from fastapi import APIRouter

from app.config.api_config import API_VERSION
from app.models.api.version_response import VersionResponse

router = APIRouter()


@router.get("/version", response_model=VersionResponse)
async def get() -> VersionResponse:
    return VersionResponse(api_version=API_VERSION)
