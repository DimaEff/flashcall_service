from fastapi import FastAPI

from models import Call
from service import flash_call

app = FastAPI(title="Call API")


@app.post("/flashcall")
async def index(payload: Call):
    call_response = flash_call(payload)
    return call_response
