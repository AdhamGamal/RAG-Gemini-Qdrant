import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Function to generate a multi-page PDF with large paragraphs
def generate_pdf(filename, title, sections):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    for section_title, text in sections.items():
        # Title
        c.setFont("Helvetica-Bold", 24)  # Bigger title
        c.drawString(72, height - 72, title)
        
        # Section title
        c.setFont("Helvetica-Bold", 20)
        c.drawString(72, height - 120, section_title)

        # Section content
        c.setFont("Helvetica", 16)  # Large text
        text_object = c.beginText(72, height - 160)
        text_object.setLeading(26)  # Line spacing
        
        # Wrap text manually into lines
        max_chars_per_line = 80
        for paragraph in text.split("\n"):
            while len(paragraph) > 0:
                line = paragraph[:max_chars_per_line]
                paragraph = paragraph[max_chars_per_line:]
                text_object.textLine(line.strip())
        c.drawText(text_object)
        
        c.showPage()  # new page for each section

    c.save()


# --- Define synthetic expanded content ---
pdfs_content = {
    "eldoria_history.pdf": (
        "History of the Kingdom of Eldoria",
        {
            "Founding Era": (
                "The Kingdom of Eldoria was founded in the year 1024 by King Arcturus I, a "
                "visionary leader who united scattered tribes into one nation. The early settlers "
                "were farmers and hunters who believed in the guiding light of the Sword of Dawn, "
                "a mythical weapon said to have been crafted by celestial beings from fallen "
                "starlight. For centuries, the people of Eldoria built vast cities of marble and "
                "stone, surrounded by fertile plains and shimmering rivers. Trade flourished, "
                "and early diplomacy established the kingdom as a beacon of civilization. "
                "Mythology tells of magical creatures that lived alongside humans during this era, "
                "contributing wisdom and protection. The founding era is remembered as a time of "
                "great unity and promise, setting the stage for the kingdom’s future prosperity."
            ),
            "Golden Age": (
                "The Golden Age of Eldoria began in the 12th century, marked by an explosion of "
                "knowledge, art, and arcane discovery. Towering libraries were filled with "
                "manuscripts on alchemy, astronomy, and medicine. The magical universities of "
                "Aurensfall attracted scholars from distant lands, who came to study alongside "
                "dragons, who shared their ancient knowledge in exchange for peace treaties. "
                "Music filled the streets, literature inspired revolutions of thought, and trade "
                "routes extended across continents. Eldoria’s armies, clad in shining armor and "
                "supported by elemental mages, defended the realm from external threats. "
                "For nearly two centuries, Eldoria stood unrivaled in power, culture, and "
                "spiritual influence, remembered as the greatest era in its long history."
            ),
            "Fall of the Kingdom": (
                "The decline of Eldoria began in the 14th century, as internal strife tore the "
                "once-united kingdom apart. Rival noble houses vied for power, sparking decades "
                "of civil war that drained the nation’s strength. The rise of the Great Shadow War "
                "further destabilized the realm, as creatures of darkness invaded the borderlands. "
                "Dragons, once steadfast allies, withdrew to their mountain strongholds, refusing "
                "to be part of human conflict. By 1453, the capital city was sacked, its great "
                "cathedrals reduced to ruins. Survivors tell of the night sky blackening as the "
                "enemy swept through the land, ending Eldoria’s thousand-year reign. What remained "
                "was a fragmented land of scattered villages, living in the shadow of a glorious "
                "past that would never return."
            ),
        },
    ),
    "quantum_drive_specs.pdf": (
        "Technical Specification of the Starlink Quantum Drive",
        {
            "Introduction": (
                "The Starlink Quantum Drive represents the pinnacle of interstellar propulsion "
                "technology. It was designed to break the barriers of relativistic travel by "
                "leveraging the fundamental properties of quantum entanglement. Unlike classical "
                "thrusters, which rely on combustion or ion propulsion, the Quantum Drive manipulates "
                "spacetime itself to shorten distances. In its earliest tests, unmanned probes "
                "were able to traverse multiple star systems in mere hours, a feat once thought "
                "impossible. The drive has since been installed on long-range exploration vessels, "
                "opening the doors to galactic colonization and research. Its creation marked the "
                "end of humanity’s reliance on generational ships and the beginning of true cosmic "
                "mobility."
            ),
            "Core Mechanism": (
                "At the core of the Starlink Quantum Drive is the Quantum Resonance Chamber (QRC). "
                "This device stabilizes entangled particles within a superconducting matrix cooled "
                "to near absolute zero. When the chamber is activated, the entangled states are "
                "manipulated to create a localized warp bubble that envelopes the vessel. Within "
                "this bubble, space itself contracts in front of the ship and expands behind it, "
                "propelling the craft forward without traditional thrust. This bypasses the need "
                "for fuel on long journeys, relying instead on the energy generated by quantum "
                "fluctuations and resonance harmonics. The QRC is supported by a lattice of "
                "subspace stabilizers that prevent collapse of the field during operation."
            ),
            "Limitations": (
                "Despite its groundbreaking design, the Quantum Drive is not without challenges. "
                "The entanglement fields require stabilization using Zirconium-X, an exotic crystal "
                "that is incredibly rare and dangerous to mine. Moreover, extended use causes "
                "thermal buildup within the resonance chamber, necessitating advanced cryogenic "
                "cooling systems to prevent catastrophic failure. Navigation also poses difficulties: "
                "ships must carefully calculate entry and exit vectors, as even small errors can "
                "lead to emergence in unstable regions of space. As such, while the drive has "
                "revolutionized space travel, it remains a technology accessible only to the most "
                "advanced civilizations."
            ),
        },
    ),
    "zirconia_recipes.pdf": (
        "Cooking Recipes from the Planet Zirconia",
        {
            "Crystal Soup": (
                "Crystal Soup is one of the most beloved traditional dishes of Zirconia. Made from "
                "ground luminous crystals that retain their sparkle even when cooked, the broth "
                "shines faintly in the dark. The dish is spiced with plasma herbs, which produce "
                "tiny sparks when stirred, giving the meal a dazzling glow. Locals believe the soup "
                "enhances stamina and sharpens the senses, making it popular among warriors before "
                "long journeys. Entire feasts are dedicated to its preparation, with families "
                "gathering to pass down recipes that vary slightly between regions."
            ),
            "Lava Cakes": (
                "Lava Cakes on Zirconia are unlike anything found on Earth. They are baked directly "
                "within volcanic ovens powered by natural magma streams. The cakes are infused with "
                "thermal berries, which retain heat for hours and create a molten core that bursts "
                "forth when cut. Travelers often risk burns to taste them fresh from the oven. "
                "Legends say that eating one during the Festival of Fire ensures good fortune for "
                "an entire year. The cakes are also traded as luxury exports, fetching immense "
                "value in off-world markets."
            ),
            "Nebula Tea": (
                "Nebula Tea is a mystical beverage brewed from vapor clouds collected high in "
                "Zirconia’s upper atmosphere. When steeped, the tea glows with a faint aura and "
                "releases fragrances that induce relaxation and lucid dreams. The Zirconians use "
                "it during twilight ceremonies, where participants drink together under the twin "
                "moons while singing songs that date back thousands of years. Many visitors claim "
                "that even a single sip allows them to see visions of distant galaxies, though "
                "whether this is scientific or spiritual remains uncertain."
            ),
        },
    ),
}

# --- Ensure data folder exists ---
os.makedirs("data", exist_ok=True)

# --- Generate the PDFs into the data/ folder ---
for filename, (title, sections) in pdfs_content.items():
    filepath = os.path.join("data", filename)
    generate_pdf(filepath, title, sections)

print("PDFs generated in 'data/' folder:", list(pdfs_content.keys()))
