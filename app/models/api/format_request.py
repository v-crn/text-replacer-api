from typing import Optional

from app.models.functions.replace_args import ReplaceArgs
from app.models.functions.replace_param import ReplaceParam


class FormatRequest(ReplaceArgs):
    text: str
    params: Optional[list[ReplaceParam]] = [ReplaceParam()]
