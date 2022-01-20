import re

from app.models.functions.replace_args import ReplaceArgs
from app.models.functions.replace_param import DEFAULT_PATTERN, ReplaceParam


def replace(args: ReplaceArgs) -> str:
    text = args.text
    params = [ReplaceParam()] if args.params is None else args.params

    for param in params:
        # acceptable: - ~ ! + , = @
        # need a delemeter (\): ^ $ | \ [ ] ( ){ }
        replacement = "_" if param.replacement is None else param.replacement
        if param.pattern is not None:
            pattern = param.pattern
        else:
            pattern = DEFAULT_PATTERN

        extra_pattern = param.extra_pattern if param.extra_pattern is not None else None
        if extra_pattern is not None:
            pattern += "|" + extra_pattern

        text = re.sub(pattern, replacement, text)

    return text
