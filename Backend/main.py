from fastapi import Depends
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_db
from routes.products import router as products_router
from routes.auth_routes import router as auth_router

app = FastAPI(
    title = 'Quantum Zone API',
    description = 'AI-Powered E-commerce Order Automation System',
    version = '1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

app.include_router(products_router)
app.include_router(auth_router)

@app.get('/')
def root():
    return {'message': 'Welcome to Quantum Zone API'}

@app.get('/health')
def health_check(db=Depends(get_db)):
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("""SELECT * FROM products""")
        products = cursor.fetchall()

        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "error_type": type(e).__name__, "details": str(e)}