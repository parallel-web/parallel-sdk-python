"""Console warnings for API calls that the Parallel API marks as deprecated.

The API flags a deprecated call with the `Deprecation` response header (RFC 9745),
optionally with `Sunset` and `Link` (`rel="deprecation"` / `rel="successor-version"`),
or with a `deprecation_warning` item in the JSON body's `warnings` list.
Each notice is shown once per process.
"""

from __future__ import annotations

import sys
import warnings
from typing import Set, Dict, List, cast

import httpx

__all__ = ["ParallelDeprecationWarning", "warn_on_deprecation_headers", "warn_on_deprecation_body"]

DEPRECATION_WARNING_TYPE = "deprecation_warning"

_seen: Set[str] = set()


class ParallelDeprecationWarning(FutureWarning):
    """A Parallel API call you made is deprecated.

    Silence it with `warnings.filterwarnings("ignore", category=ParallelDeprecationWarning)`.
    """


def warn_on_deprecation_headers(response: httpx.Response) -> None:
    if "deprecation" not in response.headers:
        return

    endpoint = f"{response.request.method} {response.url.path}"
    message = f"Parallel API: {endpoint} is deprecated"
    sunset = response.headers.get("sunset")
    if sunset:
        message += f" and will be removed after {sunset}"
    message += "."

    links = response.links
    successor = links.get("successor-version", {}).get("url")
    docs = links.get("deprecation", {}).get("url")
    if successor:
        message += f" Use {successor} instead."
    if docs:
        message += f" See {docs}"

    _emit(endpoint, message)


def warn_on_deprecation_body(data: object, response: httpx.Response) -> None:
    # The header notice already covers this response.
    if "deprecation" in response.headers or not isinstance(data, dict):
        return

    items = cast("Dict[str, object]", data).get("warnings")
    if not isinstance(items, list):
        return

    for item in cast("List[object]", items):
        if not isinstance(item, dict):
            continue
        warning = cast("Dict[str, object]", item)
        if warning.get("type") != DEPRECATION_WARNING_TYPE:
            continue

        text = str(warning.get("message") or "This call is deprecated.")
        message = f"Parallel API: {text}"
        detail = warning.get("detail")
        docs = cast("Dict[str, object]", detail).get("documentation") if isinstance(detail, dict) else None
        if docs and str(docs) not in text:
            message += f" See {docs}"
        _emit(text, message)


def _emit(key: str, message: str) -> None:
    if key in _seen:
        return
    _seen.add(key)
    warnings.warn(message, ParallelDeprecationWarning, stacklevel=_caller_stacklevel())


def _caller_stacklevel() -> int:
    """Point the warning at the first frame outside this package, i.e. the user's call."""
    package = __name__.split(".")[0]
    frame = sys._getframe(1)
    level = 1
    while frame.f_back is not None and frame.f_globals.get("__name__", "").split(".")[0] == package:
        frame = frame.f_back
        level += 1
    return level
