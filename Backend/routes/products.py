from fastapi import APIRouter, HTTPException, Depends
from database import get_db

router = APIRouter(prefix='/products', tags=['Products'])

@router.get('/')
def get_all_products(db=Depends(get_db)):
    cursor = db.cursor(dictionary=True)

    cursor.execute('''
        SELECT product_id, name, description, image_url
        FROM products
        WHERE is_active = TRUE;
    ''')

    products = cursor.fetchall()

    for product in products:
        cursor.execute('''
            SELECT
                pv.variant_id,
                pv.variant_name,
                pv.price,
                pv.image_url,
                i.quantity,
                CASE WHEN i.quantity > 0 THEN TRUE ELSE FALSE END AS in_stock
            FROM product_variants pv
            LEFT JOIN inventory i ON pv.variant_id = i.variant_id
            WHERE pv.product_id = %s AND pv.is_active = TRUE;
        ''', (product["product_id"],))

        product['variants'] = cursor.fetchall()

    cursor.close()
        
    return products

@router.get('/{product_id}')
def get_product_by_id(product_id: int, db=Depends(get_db)):
    cursor = db.cursor(dictionary=True)

    cursor.execute('''
        SELECT product_id, name, description, image_url
        FROM products
        WHERE product_id = %s AND is_active = TRUE;
    ''', (product_id,))

    product = cursor.fetchone()

    if not product:
        cursor.close()
        raise HTTPException(status_code=404, detail = 'Product not found')
    
    cursor.execute('''
        SELECT 
            pv.variant_id,
            pv.variant_name,
            pv.price,
            pv.image_url,
            i.quantity,
            CASE WHEN i.quantity > 0 THEN TRUE ELSE FALSE END AS in_stock
        FROM product_variants pv
        LEFT JOIN inventory i ON pv.variant_id = i.variant_id
        WHERE pv.product_id = %s AND pv.is_active = TRUE
    ''', (product_id,))

    product['variants'] = cursor.fetchall()

    cursor.close()
    return product