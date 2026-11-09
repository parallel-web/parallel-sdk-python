from typing import Union

import httpx

from .._types import NotGiven
from .._constants import DEFAULT_EXECUTE_TIMEOUT_SECONDS
from .._utils._utils import is_given


def prepare_timeout_float(timeout: Union[float, httpx.Timeout, None, NotGiven]) -> float:
    """Create a simple float timeout for server responses from the provided timeout.

    For httpx.Timeout, we only use the read timeout.
    """
    if isinstance(timeout, httpx.Timeout):
        timeout = timeout.read

    if not is_given(timeout) or timeout is None:
        return DEFAULT_EXECUTE_TIMEOUT_SECONDS

    return timeout
