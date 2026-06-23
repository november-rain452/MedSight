from .csv_field_parser import parse_csv_field_to_list, parse_csv_field_to_str


def transform_row(row):
    return {
        "fid": row.get("unique_id"),
        "name": parse_csv_field_to_str(row.get("name")),
        "specialties": parse_csv_field_to_list(row.get("specialties")),
        "procedure": parse_csv_field_to_list(row.get("procedure")),
        "equipment": parse_csv_field_to_list(row.get("equipment")),
        "capability": parse_csv_field_to_list(row.get("capability")),
        "description": parse_csv_field_to_str(row.get("description")),
        "location": {
            "city": parse_csv_field_to_str(row.get("address_city")),
            "country": parse_csv_field_to_str(row.get("address_country")),
        },
        "facility_type": parse_csv_field_to_str(row.get("facilityTypeId")),
    }
