# app/agents/nl_sql_agent.py

"""
Natural Language → SQL Agent

Uses:
- Ollama (llama3) locally
- OpenAI code kept COMMENTED for future use
"""

import subprocess
import json
from typing import Dict, List

# ==============================
# 🔒 OPENAI (COMMENTED FOR NOW)
# ==============================
# from openai import OpenAI
# client = OpenAI()

# def generate_sql_openai(question: str, schema: Dict[str, List[str]]) -> str:
#     prompt = f"""
#     You are an expert Snowflake SQL developer.
#
#     Schema:
#     {json.dumps(schema, indent=2)}
#
#     Question:
#     {question}
#
#     Generate ONLY SQL.
#     """
#
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#     )
#
#     return response.choices[0].message.content.strip()


# ==============================
# 🦙 OLLAMA (ACTIVE)
# ==============================

def generate_sql(question: str, schema: Dict[str, List[str]]) -> str:
    """
    Generate SQL using Llama3 via Ollama
    """

    prompt = f"""
You are an expert Snowflake SQL developer.

Schema:
{json.dumps(schema, indent=2)}

Rules:
- Use only the provided tables and columns
- Use Snowflake SQL
- Do NOT explain
- Output ONLY SQL

Question:
{question}
"""

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        capture_output=True,
        text=True
    )

    sql = result.stdout.strip()

    if not sql:
        raise RuntimeError("LLM returned empty SQL")

    return sql
