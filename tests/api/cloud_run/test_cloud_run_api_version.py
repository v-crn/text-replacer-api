import requests

from app.config.api_config import API_VERSION
from app.models.api.version_response import VersionResponse
from tests.config import VERSION_ENDPOINT


def test_versionをGETするとAPI_VERSIONが返ってくる() -> None:
    response = requests.get(url=VERSION_ENDPOINT)
    api_version = VersionResponse(**response.json()).api_version
    assert response.status_code == 200, f"Invalid response: {response.status_code}"
    assert api_version == API_VERSION, f"Invalid API_VERSION: {api_version}"
