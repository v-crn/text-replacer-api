from pydantic import BaseModel


class VersionResponse(BaseModel):
    api_version: str
