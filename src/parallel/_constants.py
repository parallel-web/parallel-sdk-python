# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import httpx

RAW_RESPONSE_HEADER = "X-Stainless-Raw-Response"
OVERRIDE_CAST_TO_HEADER = "____stainless_override_cast_to"

# default timeout for execution requests which wait for results is 1 hour.
DEFAULT_EXECUTE_TIMEOUT_SECONDS = 3600
# default timeout for http requests is 10 minutes.
DEFAULT_TIMEOUT_SECONDS = 600
DEFAULT_TIMEOUT = httpx.Timeout(timeout=DEFAULT_TIMEOUT_SECONDS, connect=5.0)
DEFAULT_MAX_RETRIES = 2
DEFAULT_CONNECTION_LIMITS = httpx.Limits(max_connections=100, max_keepalive_connections=20)
DEFAULT_POLL_INTERVAL_MS = 20000

INITIAL_RETRY_DELAY = 0.5
MAX_RETRY_DELAY = 8.0
