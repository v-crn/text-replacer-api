from pydantic import BaseModel


class FormatResponse(BaseModel):
    text: str
