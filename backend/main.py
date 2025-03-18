from fastapi import FastAPI
from auth.routes import auth_router
from user.routes import user_router


app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(user_router, prefix="/users", tags=["Users"])




@app.get("/")
async def read_root():
    return {"Hello" : "World"}