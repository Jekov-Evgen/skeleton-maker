CONST_MAIN_PY = """
from fastapi import FastAPI
from app.api.endpoints import router as api_router

app = FastAPI(
    title="FastAPI Project",
    description="Базовый шаблон проекта на FastAPI",
    version="1.0.0",
)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Project!"}
"""

CONST_ENDPOINTS_PY = """
from fastapi import APIRouter

router = APIRouter()

@router.get("/items/{item_id}", tags=["Items"])
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
"""

CONST_CONFIG_PY = """
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Project"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
"""

CONST_COMMON_PY = """
from fastapi import Depends, HTTPException

async def get_token_header(x_token: str = Header(...)):
    if x_token != "secret-token":
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
"""

CONST_USER_PY = """
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
"""

CONST_ENV = """
APP_NAME=FastAPI Project
DEBUG=True
"""

CONST_REQUIMENTS_TXT = """
fastapi==0.95.2
uvicorn==0.22.0
pydantic==1.10.8
"""

CONST_TEST_MAIN_PY = """
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI Project!"}

def test_read_item():
    response = client.get("/items/1?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": "test"}
"""