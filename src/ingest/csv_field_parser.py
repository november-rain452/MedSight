import ast
import pandas as pd


def parse_csv_field_to_list(value):
    """Converts CSV string fields into Python lists"""

    if value is None:
        return []

    str_val = str(value).strip()

    if str_val.lower() in ["", "none", "null", "nan"]:
        return []

    try:
        cleaned = str_val.replace('""', '"')
        parsed = ast.literal_eval(cleaned)

        return [v for v in parsed if str(v).lower() != "nan"]
    except Exception:
        return [
            v.strip()
            for v in str_val.split(",")
            if v.strip() and v.strip().lower() != "nan"
        ]


def parse_csv_field_to_none(value):
    """Convert invalid CSV values to None so they are stored as SQL NULL."""

    if value is None:
        return None

    if pd.isna(value):
        return None

    value = str(value).strip()

    if value.lower() in {"", "none", "null", "nan"}:
        return None

    return value
