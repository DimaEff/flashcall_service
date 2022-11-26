from fastapi import FastAPI
from pydantic import ValidationError

from models import Call, CallResponse
from routes_consts import FLASHCALL
from service import flash_call

app = FastAPI(title="Call API")


@app.post(FLASHCALL, response_model=CallResponse)
async def index(payload: Call) -> CallResponse | ValidationError:
    call_response = flash_call(payload)
    return call_response
