from fastapi import FastAPI
from auth.routes import auth_router
app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])


@app.get("/")
async def read_root():
    return {"Hello" : "World"}