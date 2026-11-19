import time
from typing import Union, NoReturn

import httpx

from .._types import NotGiven
from .._constants import INITIAL_RETRY_DELAY, DEFAULT_EXECUTE_TIMEOUT_SECONDS
from .._exceptions import APIStatusError, APITimeoutError
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


def raise_timeout(run_id: str, exc: Union[Exception, None]) -> NoReturn:
    raise TimeoutError(f"Fetching task run result for run id {run_id} timed out.") from exc


def _is_retryable_error(status_code: int) -> bool:
    """Determine if an error is retryable.

    We retry the following HTTP status codes within the SDK:
    - 408 (Request Timeout): The server timed out waiting for the request
    - 503 (Service Unavailable): The server is temporarily unable to handle the request
    - 504 (Gateway Timeout): The gateway server timed out

    These errors typically indicate temporary issues with the server or network
    that may resolve upon retry. We don't include 429 (Too Many Requests) as this
    indicates rate limiting, which requires backing off rather than immediate retries.

    Note: This is a low-level retry mechanism within the SDK. Customers may want to
    implement their own retry logic at the application level for other error types.
    """
    return status_code in (408, 503, 504)


def is_retryable_wait_error(exc: Exception) -> bool:
    """Whether a failed task run result fetch may be retried before the deadline."""
    if isinstance(exc, APITimeoutError):
        return True
    return isinstance(exc, APIStatusError) and _is_retryable_error(exc.status_code)


def delay_before_retry(exc: Exception, deadline: float) -> float:
    """Seconds to pause before fetching the result again. A timeout or 408 already
    waited for the run, so it retries at once; a 503 or 504 pauses briefly."""
    if isinstance(exc, APIStatusError) and exc.status_code != 408:
        return max(0.0, min(INITIAL_RETRY_DELAY, deadline - time.monotonic()))
    return 0.0
