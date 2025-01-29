from fastapi import HTTPException, APIRouter, Response
from models.models import UserRegisterSchema, UserLoginSchema
from JWT_settings import security, config
from db.db import connection
from logger import logger
router = APIRouter(
    tags=["authorization"],
)

conn = connection()
cur = conn.cursor()


@router.post("/registration", summary="registration form")
async def registration(creds: UserRegisterSchema):
    cur.execute("""SELECT * FROM users WHERE email = %s """, (creds.email, ))
    if cur.fetchone():
        logger.exception('Email is already registered')
        raise HTTPException(status_code=401, detail="Email is already registered")
    try:
        cur.execute("""INSERT INTO users (name, surname, email, password) VALUES (%s, %s, %s, %s);""", (creds.name, creds.surname, creds.email, creds.password))
        logger.info(f"User with email: {creds.email} successfully registered")
        conn.commit()
    except:
        conn.rollback()
        logger.exception('Wrong credentials')
        raise HTTPException(status_code=401, detail="Wrong credentials")



@router.post("/login", summary="login form")
async def login(creds: UserLoginSchema, response: Response):
    cur.execute("""SELECT id FROM users WHERE email = %s AND password = %s""", (creds.email, creds.password))
    if uid := cur.fetchone():
        logger.info(f"User {creds.email} successfully logged in")
        token = security.create_access_token(uid=f"{uid}")
        logger.info(f"Create token: {token}")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access token": uid}
    else:
        logger.exception(f"Wrong credentials by user: {creds.email}")
        raise HTTPException(status_code=401, detail="Wrong credentials")
