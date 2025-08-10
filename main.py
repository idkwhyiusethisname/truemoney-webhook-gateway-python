from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import jwt
import json,os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

# เดียยติดคอ
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/webhook")
async def webhook(request: Request):
    json_body = await request.json()

    jwt_token = json_body.get("message")
    decoded_jwt = None
    if jwt_token:
        try:
            decoded_jwt = jwt.decode(
                jwt_token,
                SECRET_KEY,
                algorithms=["HS256"],
                leeway=30  # เวลาดริฟ
            )
            
            if "amount" in decoded_jwt:
                decoded_jwt["amount"] = decoded_jwt["amount"] // 100 # ฟอแมตเลข จากหน่วยสตางค์เป็นเลขเต็ม
        except jwt.ExpiredSignatureError:
            decoded_jwt = "JWT expired"
        except jwt.InvalidTokenError as e:
            decoded_jwt = f"Invalid JWT: {str(e)}"
    
    print(decoded_jwt) # ข้อมูล
    return "OK"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=5000, reload=True)