from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from snowflake_db import get_connection

app = FastAPI()

# Allow frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later restrict to your domain
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model
class ProductRequest(BaseModel):
    productCode: str

@app.post("/product")
def get_product(req: ProductRequest):
    product_code = req.productCode.strip()
    if not product_code:
        return {"error": "productCode is required"}

    try:
        conn = get_connection()
        cur = conn.cursor()
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
        columns = [col[0] for col in cur.description]
        result = [dict(zip(columns, row)) for row in rows]

    except Exception as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

    return result
