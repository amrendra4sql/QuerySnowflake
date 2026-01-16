from fastapi import APIRouter
from pydantic import BaseModel
from app.db.snowflake_db import get_connection

router = APIRouter()

class ProductRequest(BaseModel):
    productCode: str

@router.post("/product")
def get_product(req: ProductRequest):
    product_code = req.productCode.strip()
    if not product_code:
        return {"error": "productCode is required"}

    conn = get_connection()
    cur = conn.cursor()

    try:
        sql = """
            SELECT
                PRODUCT_KEY,
                PRODUCT_CODE,
                PRODUCT_NAME,
                PRODUCT_DESC,
                CATEGORY,
                SUB_CATEGORY,
                UNIT_OF_MEASURE,
                UNIT_PRICE,
                BRAND,
                SUPPLIER_NAME,
                PRODUCT_STATUS,
                LAUNCH_DATE
            FROM DIM_PRODUCT
            WHERE PRODUCT_CODE = %s
        """
        cur.execute(sql, (product_code,))
        rows = cur.fetchall()
        columns = [c[0] for c in cur.description]
        return [dict(zip(columns, row)) for row in rows]

    finally:
        cur.close()
        conn.close()
