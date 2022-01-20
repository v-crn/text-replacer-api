from fastapi import APIRouter

from app.api.routes import format, version

router = APIRouter()

router.include_router(format.router, tags=["format"])
router.include_router(version.router, tags=["version"])
