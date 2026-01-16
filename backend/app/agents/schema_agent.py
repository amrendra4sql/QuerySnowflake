# app/agents/schema_agent.py
from typing import List, Dict
from app.db.snowflake_db import get_connection

def get_schema_context(tables: List[str] = None) -> Dict[str, List[str]]:
    """
    Fetch schema from Snowflake and return as dict:
    { table_name: [column1, column2, ...] }
    """

    if tables:
        table_list = ", ".join(f"'{t}'" for t in tables)
        table_filter = f"AND table_name IN ({table_list})"
    else:
        table_filter = ""

    query = f"""
        SELECT table_name, column_name
        FROM information_schema.columns
        WHERE table_schema = 'PUBLIC'
        {table_filter}
        ORDER BY table_name, ordinal_position
    """

    schema: Dict[str, List[str]] = {}
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        for table_name, column_name in rows:
            schema.setdefault(table_name, []).append(column_name)
    finally:
        cur.close()
        conn.close()

    return schema
