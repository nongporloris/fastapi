from fastapi import FastAPI
from typing import Optional
import uvicorn
from pydantic import BaseModel
from typing import Union


class Data(BaseModel):
    name: str
    password: str
    nickname: Optional[str] = None


app = FastAPI()


@app.get("/manpage")
async def main_page_get():
    data = {
        'Your are': 'tempname',
        'Your pass': 'temppass',
        'nickname is': 'tempnickname',
    }

    return data


@app.post("/manpage1")
async def main_page_post(request: Data):
    data = {
        'Your name': request.name,
        'Your pass': request.password,
        'Your nickname': request.nickname,
    }
    print(data)
    return data


@app.put("/manpage")
async def main_page_put(request: Data):
    data = {
        'Your name': request.name,
        'Your pass': request.password,
        'Your nickname': request.nickname,
    }
    return data
