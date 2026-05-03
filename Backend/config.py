from dotenv import load_dotenv
import os

load_dotenv() # Load variables into memory

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', '3306'))
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_NAME = os.getenv('DB_NAME', 'quantum_zone_db')
JWT_SECRET = os.getenv('JWT_SECRET', 'default-secret')
N8N_WEBHOOK_URL = os.getenv('N8N_WEBHOOK_URL', '')