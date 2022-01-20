import requests

from tests.config import FORMAT_ENDPOINT

data = {
    "text": (
        "Error!: Wow, [Error] is an hungolomghononoloughongous "
        "error of Unga Bunga Bunga. 「エラーです@あ。」¥"
    ),
    "params": [
        {"replacement": "", "extra_pattern": "「|」|【|】|，|．"},
        {"replacement": "", "pattern": "sample!"},
        {"replacement": "🍣", "pattern": r"@|あ|。"},
    ],
}


def test_formatに正しいリクエストをPOSTすると200が返ってくる() -> None:
    response = requests.post(url=FORMAT_ENDPOINT, json=data)
    assert response.status_code == 200, f"Invalid response: {response.status_code}"


def test_format_textのkeyが不正の場合422AsersionErrorが返ってくる() -> None:
    data = {
        "a": "こんにちは！",
        "params": [
            {"replacement": "🐧"},
        ],
    }
    response = requests.post(url=FORMAT_ENDPOINT, json=data)
    print(f"response.text: {response.text}")
    assert response.status_code == 422, f"Invalid response: {response.status_code}"


def test_format_textのvalueが不正の場合422AsersionErrorが返ってくる() -> None:
    data = {
        "a": 1,
        "params": [
            {"replacement": "🐧"},
        ],
    }
    response = requests.post(url=FORMAT_ENDPOINT, json=data)
    print(f"response.text: {response.text}")
    assert response.status_code == 422, f"Invalid response: {response.status_code}"


def test_format_paramsのkeyが不正の場合は無視されて200が返ってくる() -> None:
    data = {"text": "<あ> ,[い].。", "🍏": [{"replacement": "🐧"}]}
    response = requests.post(url=FORMAT_ENDPOINT, json=data)
    print(f"response.text: {response.text}")
    assert response.status_code == 200, f"Invalid response: {response.status_code}"


def test_format_paramsのvalueが不正の場合422AsersionErrorが返ってくる() -> None:
    data = {"text": "<あ> ,[い].。", "params": "💀"}
    response = requests.post(url=FORMAT_ENDPOINT, json=data)
    print(f"response.text: {response.text}")
    assert response.status_code == 422, f"Invalid response: {response.status_code}"
