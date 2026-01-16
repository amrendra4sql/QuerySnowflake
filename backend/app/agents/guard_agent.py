import re

FORBIDDEN = r"\b(insert|update|delete|merge|drop|alter|truncate|create)\b"

def validate_sql(sql: str) -> str:
    sql = sql.strip().rstrip(";")

    if not sql.lower().startswith("select"):
        raise ValueError("Only SELECT queries allowed")

    if re.search(FORBIDDEN, sql.lower()):
        raise ValueError("Forbidden SQL detected")

    if "limit" not in sql.lower():
        sql += " LIMIT 100"

    return sql
