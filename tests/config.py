import os

URL = "https://text-replacer-api-gshrf35fa-wd.b.run.app"
FORMAT_ENDPOINT = os.path.join(URL, "format")
VERSION_ENDPOINT = os.path.join(URL, "version")

SAMPLE_TEXT = (
    "Error: Failure while executing; `git clone "
    "https://github.com/Homebrew/linuxbrew-core "
    "/home/linuxbrew/.linuxbrew/Homebrew/Library"
    "/Taps/homebrew/homebrew-core` exited with 128."
)
DEFAULT_REPLACED_TEXT = (
    "Error__Failure_while_executing___git_clone_https___github_com_"
    "Homebrew_linuxbrew-core__home_linuxbrew__linuxbrew_Homebrew_Library_"
    "Taps_homebrew_homebrew-core__exited_with_128_"
)
