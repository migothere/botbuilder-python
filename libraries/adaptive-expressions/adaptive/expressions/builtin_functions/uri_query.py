from urllib.parse import urlparse
from ..options import Options
from ..expression_type import URIQUERY
from ..function_utils import FunctionUtils
from ..return_type import ReturnType
from ..expression_evaluator import ExpressionEvaluator


class UriQuery(ExpressionEvaluator):
    def __init__(self):
        super().__init__(
            URIQUERY,
            UriQuery.evaluator,
            ReturnType.String,
            FunctionUtils.validate_unary_string,
        )

    @staticmethod
    def evaluator(expression: object, state, options: Options):
        value: object = None
        error: str = None
        args: list
        args, error = FunctionUtils.evaluate_children(expression, state, options)
        if error is None:
            if isinstance(args[0], str):
                parsed = urlparse(args[0])
                value = "?" + parsed.query
            else:
                error = "${args[0]} should be a string."
        return value, error
