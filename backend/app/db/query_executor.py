from app.db.snowflake_db import get_connection

def execute_query(sql: str):
    conn = get_connection()
    print(f"[DEBUG] Snowflake connection params:")
    print(f"  ACCOUNT={conn.account}")
    print(f"  USER={conn.user}")
    print(f"  WAREHOUSE={conn.warehouse}")
    print(f"  DATABASE={conn.database}")
    print(f"  SCHEMA={conn.schema}")
    print(f"  ROLE={conn.role}")
    cur = conn.cursor()

    cur.execute(sql)
    rows = cur.fetchall()
    columns = [c[0] for c in cur.description]

    cur.close()
    conn.close()

    return [dict(zip(columns, row)) for row in rows]
