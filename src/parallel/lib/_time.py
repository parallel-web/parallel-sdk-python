import time
import contextlib
from typing import Union, Iterator, NoReturn

import httpx

from .._types import NotGiven
from .._constants import DEFAULT_TIMEOUT_SECONDS
from .._exceptions import APIStatusError, APITimeoutError
from .._utils._utils import is_given


def prepare_timeout_float(timeout: Union[float, httpx.Timeout, None, NotGiven]) -> float:
    """Create a simple float timeout for server responses from the provided timeout.

    For httpx.Timeout, we only use the read timeout.
    """
    if isinstance(timeout, httpx.Timeout):
        timeout = timeout.read

    if not is_given(timeout) or timeout is None:
        return DEFAULT_TIMEOUT_SECONDS

    return timeout


def _raise_timeout(run_id: str, exc: Union[Exception, None]) -> NoReturn:
    raise TimeoutError(f"Fetching task run result for run id {run_id} timed out.") from exc


def _is_retryable_error(status_code: int) -> bool:
    """Determine if an error is retryable."""
    return status_code in (408, 503, 504)


@contextlib.contextmanager
def timeout_retry_context(run_id: str, deadline: float) -> Iterator[None]:
    """Context manager for handling timeouts and retries when fetching task run results.

    Args:
        run_id: The ID of the task run
        deadline: The absolute time (monotonic) by which the operation must complete

    Raises:
        TimeoutError: If the deadline is reached
        APIStatusError: For non-timeout API errors
    """
    exc: Union[Exception, None] = None
    while time.monotonic() < deadline:
        try:
            yield
            return
        except APITimeoutError as e:
            exc = e
            continue
        except APIStatusError as e:
            if _is_retryable_error(e.status_code):
                exc = e
                continue
            raise
    _raise_timeout(run_id, exc)
