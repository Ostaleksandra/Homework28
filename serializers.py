from datetime import datetime
from pydantic import BaseModel, Field

class AuthRequest(BaseModel):
    username: constr(strict=True)
    password: constr(strict=True)

class AuthToken(BaseModel):
    token:str

class Booking(BaseModel):
    firstname: str = Field(...)
    lastname: str = Field(...)
    totalprice: int = Field(...)
    depositpaid: bool = Field(...)
    checkin: datetime = Field(...)
    checkout: datetime = Field(...)
    additionalneeds: str = Field(None)


