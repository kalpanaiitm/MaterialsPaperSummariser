"""Deterministic passage selection; never invents scientific findings."""
import re

CATEGORIES = {
    "Synthesis": ("synthesis", "prepared", "reaction", "heated"),
    "Structure and characterisation": ("xrd", "diffraction", "crystal", "structure"),
    "Optical properties": ("luminescence", "emission", "photoluminescence", "optical"),
}

def summarise_text(text: str) -> dict[str, str]:
    passages = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"(?<=[.!?])\s+", text)]
    return {
        category: next((p[:500] for p in passages if any(re.search(r"\b" + re.escape(term) + r"\b", p, re.I) for term in terms)), "")
        for category, terms in CATEGORIES.items()
    }
