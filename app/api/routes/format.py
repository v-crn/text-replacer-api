from fastapi import APIRouter

from app.functions.replacer import replace
from app.models.api.format_request import FormatRequest
from app.models.api.format_response import FormatResponse
from app.models.functions.replace_args import ReplaceArgs

router = APIRouter()


@router.post("/format", response_model=FormatResponse)
async def post(request: FormatRequest) -> FormatResponse:
    args = ReplaceArgs(text=request.text, params=request.params)
    text = replace(args=args)

    return FormatResponse(text=text)
