from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from dotenv import load_dotenv
import os

load_dotenv()  # load .env

SECRET_KEY = os.getenv("SECRET_KEY")  # use Django SECRET_KEY
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

app = FastAPI()
security = HTTPBearer()

def get_current_user(token: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/protected")
def protected_route(user=Depends(get_current_user)):
    return {"message": f"Hello {user['user_id']}"}
