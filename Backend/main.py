from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

@app.get('/')
def root():
    return {'message': 'Welcome to Quantum Zone API'}

@app.get('/health')
def health_check():
    import mysql.connector
    from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()
        cursor.execute('SELECT 1')
        cursor.fetchone()
        cursor.close()
        connection.close()

        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "error_type": type(e).__name__, "details": str(e)}