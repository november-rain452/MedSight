from .csv_field_parser import parse_csv_field_to_list, parse_csv_field_to_none


def transform_row(row):
    return {
        "fid": parse_csv_field_to_none(row.get("unique_id")),
        "name": parse_csv_field_to_none(row.get("name")),
        "specialties": parse_csv_field_to_list(row.get("specialties")),
        "procedure": parse_csv_field_to_list(row.get("procedure")),
        "equipment": parse_csv_field_to_list(row.get("equipment")),
        "capability": parse_csv_field_to_list(row.get("capability")),
        "organization_type": parse_csv_field_to_none(row.get("organization_type")),
        "description": parse_csv_field_to_none(row.get("description")),
        "location": {
            "city": parse_csv_field_to_none(row.get("address_city")),
            "country": parse_csv_field_to_none(row.get("address_country")),
        },
        "facility_type": parse_csv_field_to_none(row.get("facilityTypeId")),
    }


def transform_row_to_facility(row):
    return {
        "fid": row["fid"],
        "name": row["name"],
        "specialties": row["specialties"],
        "procedure": row["procedure"],
        "equipment": row["equipment"],
        "capability": row["capability"],
        "organization_type": row["organization_type"],
        "city": row["location"]["city"],
        "country": row["location"]["country"],
        "facility_type": row["facility_type"],
    }
