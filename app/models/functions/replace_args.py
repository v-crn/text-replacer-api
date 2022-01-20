from typing import Optional

from pydantic import BaseModel

from app.models.functions.replace_param import ReplaceParam


class ReplaceArgs(BaseModel):
    text: str
    params: Optional[list[ReplaceParam]] = [ReplaceParam()]
