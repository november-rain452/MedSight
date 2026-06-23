import ast


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


def parse_csv_field_to_str(value):
    """Processes CSV fields into strings safely"""

    if value is None:
        return ""

    str_val = str(value).strip()

    if str_val.lower() in ["", "none", "null", "nan"]:
        return ""

    return str_val.strip()
