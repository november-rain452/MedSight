from .csv_field_parser import parse_csv_field_to_list, parse_csv_field_to_none


def transform_row(row):
    return {
        "fid": parse_csv_field_to_none(row.unique_id),
        "name": parse_csv_field_to_none(row.name),
        "specialties": parse_csv_field_to_list(row.specialties),
        "procedure": parse_csv_field_to_list(row.procedure),
        "equipment": parse_csv_field_to_list(row.equipment),
        "capability": parse_csv_field_to_list(row.capability),
        "organization_type": parse_csv_field_to_none(row.organization_type),
        "description": parse_csv_field_to_none(row.description),
        "location": {
            "city": parse_csv_field_to_none(row.address_city),
            "country": parse_csv_field_to_none(row.address_country),
        },
        "facility_type": parse_csv_field_to_none(row.facilityTypeId),
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
