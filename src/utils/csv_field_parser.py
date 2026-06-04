import ast


def parse_csv_field_to_list(value):
    """Converts CSV string fields into Python lists"""

    if value is None:
        return []

    str_val = str(value).strip()

    if str_val in ["", "None", "null"]:
        return []

    try:
        cleaned = str_val.replace('""', '"')
        return ast.literal_eval(cleaned)
    except Exception:
        return [v.strip() for v in value.split(",") if v.strip()]
