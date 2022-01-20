from app.functions.replacer import replace
from app.models.functions.replace_args import ReplaceArgs
from app.models.functions.replace_param import ReplaceParam
from tests.config import DEFAULT_REPLACED_TEXT, SAMPLE_TEXT


def test_replace_params_keyがない場合_標準設定の置換文字列を返す() -> None:
    replace_args = ReplaceArgs.parse_obj({"text": SAMPLE_TEXT})
    text = replace(replace_args)
    print(f"text: {text}")
    assert text == DEFAULT_REPLACED_TEXT


def test_replace_paramsがNoneの場合_標準設定の置換文字列を返す() -> None:
    replace_args = ReplaceArgs.parse_obj(
        {
            "text": SAMPLE_TEXT,
            "params": None,
        }
    )
    text = replace(replace_args)
    print(f"text: {text}")
    assert text == DEFAULT_REPLACED_TEXT


def test_replace_paramsにReplaceParamインスタンスを指定して置換文字列を返す() -> None:
    replace_args = ReplaceArgs.parse_obj(
        {"text": SAMPLE_TEXT, "params": [ReplaceParam()]}
    )
    text = replace(replace_args)
    print(f"text: {text}")
    assert text == DEFAULT_REPLACED_TEXT


def test_replace_replacementを指定して置換文字列を返す() -> None:
    replace_args = ReplaceArgs.parse_obj(
        {"text": SAMPLE_TEXT, "params": [{"replacement": "🐶"}]}
    )
    correct_text = (
        "Error🐶🐶Failure🐶while🐶executing🐶🐶🐶git🐶clone🐶https🐶🐶🐶github🐶com🐶Homebrew🐶linuxbr"
        "ew-core🐶🐶home🐶linuxbrew🐶🐶linuxbrew🐶Homebrew🐶Library🐶Taps🐶homebrew🐶homebrew-cor"
        "e🐶🐶exited🐶with🐶128🐶"
    )
    text = replace(replace_args)
    print(f"text: {text}")
    assert text == correct_text


def test_replace_patternを指定して置換文字列を返す() -> None:
    replace_args = ReplaceArgs.parse_obj(
        {"text": SAMPLE_TEXT, "params": [{"pattern": r":|\/"}]}
    )
    correct_text = (
        "Error_ Failure while executing; `git clone https___github.com_Homebrew_linuxbr"
        "ew-core _home_linuxbrew_.linuxbrew_Homebrew_Library_Taps_homebrew_homebrew-cor"
        "e` exited with 128."
    )
    text = replace(replace_args)
    print(f"text: {text}")
    assert text == correct_text


def test_replace_extra_patternを指定して置換文字列を返す() -> None:
    replace_args = ReplaceArgs.parse_obj(
        {"text": SAMPLE_TEXT, "params": [{"extra_pattern": r"\d|Error"}]}
    )
    correct_text = (
        "___Failure_while_executing___git_clone_https___github_com_Homebrew_linuxbrew-"
        "core__home_linuxbrew__linuxbrew_Homebrew_Library_Taps_homebrew_homebrew-core"
        "__exited_with_____"
    )
    text = replace(replace_args)
    print(f"text: {text}")
    assert text == correct_text


def test_replace_複数のparamを指定して置換文字列を返す() -> None:
    replace_args = ReplaceArgs.parse_obj(
        {
            "text": SAMPLE_TEXT,
            "params": [
                {"replacement": "😾", "pattern": r"c|a|t"},
                {"replacement": "🐶", "pattern": r"\d|o|g"},
                {"replacement": "🐸", "pattern": r"f|r|o|g|"},
                {"replacement": "🐍", "pattern": r"p|y|t|h|o|n"},
                {"replacement": "", "extra_pattern": r"[a-zA-Z]|-|🐸"},
            ],
        }
    )
    correct_text = "🐶😾🐍😾😾🐍🐶🐶😾😾🐶🐍🐍😾😾🐍🐶😾🐍😾🐶🐶🐍😾🐶🐍🐶🐍🐍🐶😾🐍😾🐍🐍🐶🐍🐶😾🐶😾😾🐍🐶🐶🐶"
    text = replace(replace_args)
    print(f"text: {text}")
    assert text == correct_text
