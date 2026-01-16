NL_SQL_PROMPT = """
You are a Snowflake SQL expert.

Schema:
{schema}

Rules:
- Generate ONLY SELECT queries
- Use only provided tables and columns
- No explanation, output SQL only

User question:
{question}

SQL:
"""
