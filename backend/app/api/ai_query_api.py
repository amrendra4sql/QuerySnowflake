from fastapi import APIRouter
from app.models.request_models import AIQueryRequest
from app.agents.schema_agent import get_schema_context
from app.agents.nl_sql_agent import generate_sql
from app.agents.guard_agent import validate_sql
from app.db.query_executor import execute_query

router = APIRouter()

@router.post("/ai-query")
def ai_query(req: AIQueryRequest):
    # Fetch schema dynamically, no table list needed
    schema = get_schema_context()  # fetch all tables

    # Generate SQL from the AI based on question and schema
    sql = generate_sql(req.question, schema)

    # Validate SQL for safety
    safe_sql = validate_sql(sql)

    # Execute query in DB
    data = execute_query(safe_sql)

    return {
        "sql": safe_sql,
        "data": data
    }
