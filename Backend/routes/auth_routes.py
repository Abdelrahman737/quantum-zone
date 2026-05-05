from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from auth import hash_password, verify_password, create_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post('/register')
def register(data: dict, db=Depends(get_db)):
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        """SELECT customer_id FROM customers
        WHERE email = %s;""",
        (data['email'],)
    )

    if cursor.fetchone():
        cursor.close()
        raise HTTPException(status_code=400, detail='Email already registered')
    
    hashed = hash_password(data['password'])

    cursor.execute(
        """INSERT INTO customers (first_name, last_name, email, phone, password_hash)
        VALUES (%s, %s, %s, %s, %s);""",
        (data['first_name'], data['last_name'], data['email'], data['phone'], hashed)    
    )

    db.commit()
    customer_id = cursor.lastrowid
    cursor.close()

    token = create_token({'id': customer_id, 'role': 'customer'})

    return {
        'token': token,
        'user': {
            'id': customer_id,
            'name': f"{data['first_name']} {data['last_name']}",
            'role': 'customer'
        }
    }

@router.post('/login')
def login(data: dict, db=Depends(get_db)):
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT customer_id, first_name, last_name, password_hash FROM customers
        WHERE email = %s;
        """, (data['email'],)
    )

    user = cursor.fetchone()

    if user and verify_password(data['password'], user['password_hash']):
        cursor.close()
        token = create_token({'id': user['customer_id'], 'role': 'customer'})

        return {
            'token': token,
            'user': {
                'id': user['customer_id'],
                'name': f'{user['first_name']} {user['last_name']}',
                'role': 'customer'
            }
        }
    
    cursor.execute(
        "SELECT admin_id, username, password_hash FROM admins WHERE username = %s OR email = %s",
        (data["email"], data["email"])
    )

    admin = cursor.fetchone()
    if admin and verify_password(data["password"], admin["password_hash"]):
        cursor.close()
        token = create_token({"id": admin["admin_id"], "role": "admin"})
        return {
            "token": token,
            "user": {
                "id": admin["admin_id"],
                "name": admin["username"],
                "role": "admin"
            }
        }
    cursor.close()
    raise HTTPException(status_code=401, detail="Invalid email or password")
