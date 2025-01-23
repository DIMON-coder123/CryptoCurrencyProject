from fastapi import HTTPException, APIRouter, Response
from src.models.models import UserRegisterSchema, UserLoginSchema
from src.JWT_settings import security, config
from src.db.db import connection
router = APIRouter(
    tags=["authorization"],
)

conn = connection()
cur = conn.cursor()

# def main():
#
#     cur.execute("""SELECT * FROM users WHERE email = 'user@example.com';""")
#     for row in cur.fetchall():
#         print(row)

@router.post("/registration", summary="registration form")
async def registration(creds: UserRegisterSchema, response: Response):
    cur.execute("""SELECT * FROM users WHERE email = %s """, (creds.email, ))
    if cur.fetchone():
        raise HTTPException(status_code=401, detail="Email is already registered")

    try:
        cur.execute("""INSERT INTO users (name, surname, email, password) VALUES (%s, %s, %s, %s);""", (creds.name, creds.surname, creds.email, creds.password))
        conn.commit()
    except Exception:
        conn.rollback()
        raise HTTPException(status_code=401, detail="Wrong credentials")




@router.post("/login", summary="login form")
async def login(creds: UserLoginSchema, response: Response):
    if creds.email == "example@email.com" and creds.password == "test_test":
        token = security.create_access_token(uid="12345")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access token": token}
    raise HTTPException(status_code=401, detail="Incorrect email or password")

# if __name__ == "__main__":
#     main()