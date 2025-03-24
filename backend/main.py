from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.routes import auth_router
from user.routes import user_router
from password.routes import password_router

app = FastAPI()

origins = ["http://localhost:5173", "http://127.0.0.1:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(password_router, prefix="/passwords", tags=["Passwords"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
