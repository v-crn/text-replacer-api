# Text Replacer API

## 概要

- 本プロジェクトは指定した文字列を置換する API です
- デフォルト設定では文字列の中の半角スペースや記号をアンダースコア `_` に一括置換します
- 置換元の文字列には正規表現を使用することもできます

## 開発環境構築

1. 環境変数の設定

    makefiles/env.mk で定義している `_PROJECT` などの環境変数を設定する

2. docker コンテナ起動

    ```sh
    make build
    ```

3. アプリケーション起動

    ```sh
    make up
    ```

## Cloud Run へのデプロイ

```sh
make deploy
```

## Endpoints

- format
  - メインのエンドポイント
- version
  - API のバージョンを示す
- docs
  - FastAPI により自動作成された API ドキュメント
  - "Try it out" からリクエストを送ることができる

## API reference

### デフォルト設定での置換

Request:

```json
{
  "text": "Error: Failure while executing; `git clone https://github.com/Homebrew/linuxbrew-core/home/linuxbrew/.linuxbrew/Homebrew/Library/Taps/homebrew/homebrew-core` exited with 128."
}
```

Response:

```json
{
  "text": "Error__Failure_while_executing___git_clone_https___github_com_Homebrew_linuxbrew-core_home_linuxbrew__linuxbrew_Homebrew_Library_Taps_homebrew_homebrew-core__exited_with_128_"
}
```

### 置換パターンが複数ある場合

以下に示す `params` の要素を指定することで様々な置換パターンを扱うことができます。

- `replacement`
  - 置換先文字列
  - `replacement: Optional[str] = "_"`
- `pattern`
  - 置換元の正規表現
  - `pattern: Optional[str] = DEFAULT_PATTERN`
  - `DEFAULT_PATTERN`: `r" |\u3000|\.|\,|:|;|\$|\/|=|\^|\\|\[|\]|\(|\)|\{|\}|\||\n|\t|\r|\n|¥|！|\?|\?|？|⁉|#|＃|…|←|→|↑|↓|♪|♫|♬|♥|♡|▲|△|▼|▽|★|☆|■|□|◆|◇|●|○"`
- `extra_pattern`
  - デフォルトの置換元に追加したい正規表現
  - `extra_pattern: Optional[str] = None`

Request:

```json
{
  "text": "Error: Failure while executing; `git clone https://github.com/Homebrew/linuxbrew-core/home/linuxbrew/.linuxbrew/Homebrew/Library/Taps/homebrew/homebrew-core` exited with 128.",
  "params": [
    { "replacement": "😾", "pattern": "c|a|t" },
    { "replacement": "🐶", "pattern": "\\d|o|g" },
    { "replacement": "🐸", "pattern": "f|r|o|g|" },
    { "replacement": "🐍", "pattern": "p|y|t|h|o|n" },
    { "replacement": "", "extra_pattern": "[a-zA-Z]|-|🐸" }
  ]
}
```

※ json 形式のリクエストでは最後の要素の後ろに `,` を入れるとエラーになることに注意！

Response:

```json
{
  "text": "🐶😾🐍😾😾🐍🐶🐶😾😾🐶🐍🐍😾😾🐍🐶😾🐍😾🐶🐶🐍😾🐶🐍🐶🐍🐍🐶😾🐍😾🐍🐍🐶🐍🐶😾🐶😾😾🐍🐶🐶🐶"
}
```

## curl

`curl` コマンドを使う場合の例

### /version

```console
$ curl http://0.0.0.0:8080/version
{"api_version":"1.0.0"}
```

### /format

```console
$ curl http://0.0.0.0:8080/format -X POST -H "Content-Type: application/json" --data '{"text": "Error: Failure while executing; `git clone https://github.com/Homebrew/linuxbrew-core /home/linuxbrew/.linuxbrew/Homebrew/Library/Taps/homebrew/homebrew-core` exited with 128."}'
{"text":"Error__Failure_while_executing___git_clone_https___github_com_Homebrew_linuxbrew-core__home_linuxbrew__linuxbrew_Homebrew_Library_Taps_homebrew_homebrew-core__exited_with_128_"}
```
