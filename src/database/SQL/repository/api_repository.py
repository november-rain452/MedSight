from sqlalchemy.orm import Session


def execute_statement_repository(db: Session, statement):
    result = db.execute(statement)

    if result is None:
        return None

    return result
