import bcrypt
import bcrypt
from jose import jwt
from datetime import datetime, timedelta
from config import JWT_SECRET

ALGORITHM = "HS256"
TOKEN_EXPIRE_HOURS = 24

def hash_password(password: str) -> str:
    """Hash a plain text password bcrypt"""

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed.decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """Check if a plain text password matches the hashed version"""

    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def create_token(data: dict) -> str:
    """Create a JWT token with an expiry date"""
    
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=TOKEN_EXPIRE_HOURS)
    to_encode['exp'] = expire
    token = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)

    return token

def decode_token(token: str) -> dict:
    """Decode and verify a JWT token"""
    return jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
