from enum import Enum

from pydantic import validator, Field
from pydantic.main import BaseModel

CODE_LENGTH = 4
PHONE_NUMBER_REGEX = "^[0-9]{10}$"


class SupportedCountriesCodes(Enum):
    Russia = 7


def get_supported_countries_codes() -> list:
    return list(SupportedCountriesCodes._value2member_map_.keys())


class Call(BaseModel):
    country_code: int
    phone_number: str = Field(regex=PHONE_NUMBER_REGEX)
    code: int

    @validator('country_code')
    def is_supported_country_code(cls, value: int) -> int:
        supported_countries = get_supported_countries_codes()
        if value not in supported_countries:
            raise ValueError(f"This country code: {value} is not supported. You can find supported countries codes on ...")

        return value

    @validator('code')
    def code_length(cls, value: int) -> int:
        if len(str(value)) != CODE_LENGTH:
            raise ValueError(f"The length of the code must be {CODE_LENGTH}")

        return value


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
