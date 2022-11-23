from pydantic.main import BaseModel


class Call(BaseModel):
    phone_number: str
    code: int


class _CallData:
    status: int
    code: str
    phone: str
    cost: str
    timeCreate: int
    timeUpdate: str
    id: int


class CallResponse:
    success: bool
    data: _CallData
    message: str or None
