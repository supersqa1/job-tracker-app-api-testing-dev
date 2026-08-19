"""
Parametrized negative tests for rejecting invalid application status values.
"""

import pytest

from clients.api_client import APIClient
from helpers.application_helper import build_create_application_payload
from helpers.application_helper import create_application

INVALID_STATUSES = [
    "not_a_status",
    "pending",
    "random",
    "12345",
    "active",
    "",
]


@pytest.mark.parametrize("invalid_status", INVALID_STATUSES)
def test_verify_create_application_rejects_invalid_status(invalid_status):
    """Verify creating an application with an invalid status returns 422."""
    api_client = APIClient()

    payload = build_create_application_payload(status=invalid_status)
    response = create_application(api_client, payload=payload, expected_status_code=422)

    assert response["error"], (
        f"Expected error response for status '{invalid_status}' but got none"
    )
    assert response["error"]["code"] == "VALIDATION_ERROR"