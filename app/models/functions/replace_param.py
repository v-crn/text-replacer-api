from typing import Optional

from pydantic import BaseModel

from app.models.functions.regex_pattern import DEFAULT_PATTERN


class ReplaceParam(BaseModel):
    replacement: Optional[str] = "_"
    pattern: Optional[str] = DEFAULT_PATTERN
    extra_pattern: Optional[str] = None
