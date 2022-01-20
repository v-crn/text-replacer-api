from fastapi.testclient import TestClient

from app.config.api_config import API_VERSION
from app.main import app
from app.models.api.version_response import VersionResponse

client = TestClient(app)


def test_versionをGETするとAPI_VERSIONが返ってくる() -> None:
    response = client.get("/version")
    api_version = VersionResponse(**response.json()).api_version
    assert response.status_code == 200, f"Invalid response: {response.status_code}"
    assert api_version == API_VERSION, f"Invalid API_VERSION: {api_version}"
