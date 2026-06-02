# src/extraction/extractor.py

from typing import Dict, Any


def extract_facility_data(text: str) -> Dict[str, Any]:

    # For now, mock extraction (we will plug LLM later)

    # TEMP: simulate output
    return {
        "equipment": ["CT scanner"],
        "procedure": [],
        "capability": ["emergency services"],
    }
