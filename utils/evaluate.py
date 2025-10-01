# utils/evaluate.py
from typing import List, Dict
from rouge import Rouge
import bert_score
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk.translate.meteor_score import single_meteor_score
import numpy as np

# Retriever metrics helpers
def recall_at_k(pred_docs: List[List[str]], true_docs: List[List[str]], k: int = 3):
    recalls = []
    for pred, true in zip(pred_docs, true_docs):
        topk = pred[:k]
        intersection = len(set(topk) & set(true))
        recalls.append(intersection / len(true) if true else 0.0)
    return np.mean(recalls)

def precision_at_k(pred_docs: List[List[str]], true_docs: List[List[str]], k: int = 3):
    precisions = []
    for pred, true in zip(pred_docs, true_docs):
        topk = pred[:k]
        intersection = len(set(topk) & set(true))
        precisions.append(intersection / k)
    return np.mean(precisions)

def mean_reciprocal_rank(pred_docs: List[List[str]], true_docs: List[List[str]]):
    rr_scores = []
    for pred, true in zip(pred_docs, true_docs):
        score = 0.0
        for i, p in enumerate(pred):
            if p in true:
                score = 1 / (i + 1)
                break
        rr_scores.append(score)
    return np.mean(rr_scores)

# Main evaluation function
def evaluate_rag(
    rag_chain,
    eval_queries: List[Dict[str, str]],
    metrics: List[str] = [
        "exact_match", "rouge", "bert", "bleu", "meteor"
    ]
):
    """
    Evaluate a RAG chain on a list of queries with expected answers.
    Supports text metrics and can be extended for retriever metrics.

    Args:
        rag_chain: The RAG pipeline (LCEL chain).
        eval_queries: List of dicts with keys: "query" and "expected_answer".
        metrics: List of metrics to compute. Options: 
            - "exact_match", "rouge", "bert", "bleu", "meteor"

    Returns:
        results: List of dicts with query, generated answer, expected answer, and metrics.
    """
    results = []

    rouge = Rouge() if "rouge" in metrics else None
    smooth_fn = SmoothingFunction().method1

    for q in eval_queries:
        generated = rag_chain.invoke(q["query"])
        result = {
            "query": q["query"],
            "generated": generated,
            "expected": q["expected_answer"],
            "metrics": {}
        }

        # Exact Match
        if "exact_match" in metrics:
            result["metrics"]["exact_match"] = int(generated.strip() == q["expected_answer"].strip())

        # ROUGE
        if "rouge" in metrics:
            try:
                result["metrics"]["rouge"] = rouge.get_scores(generated, q["expected_answer"])[0]
            except Exception as e:
                result["metrics"]["rouge"] = str(e)

        # BERTScore
        if "bert" in metrics:
            try:
                P, R, F1 = bert_score.score([generated], [q["expected_answer"]], lang="en")
                result["metrics"]["bert_f1"] = F1.mean().item()
            except Exception as e:
                result["metrics"]["bert_f1"] = str(e)

        # BLEU
        if "bleu" in metrics:
            try:
                reference = [q["expected_answer"].split()]
                candidate = generated.split()
                result["metrics"]["bleu"] = sentence_bleu(reference, candidate, smoothing_function=smooth_fn)
            except Exception as e:
                result["metrics"]["bleu"] = str(e)

        # METEOR
        if "meteor" in metrics:
            try:
                result["metrics"]["meteor"] = single_meteor_score(q["expected_answer"], generated)
            except Exception as e:
                result["metrics"]["meteor"] = str(e)

        results.append(result)

    return results
