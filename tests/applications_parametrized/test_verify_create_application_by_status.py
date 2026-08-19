"""
Parametrized tests for creating applications with different status values.
"""

import pytest

from clients.api_client import APIClient
from helpers.application_helper import build_create_application_payload
from helpers.application_helper import create_application
from helpers.application_helper import delete_application

VALID_STATUSES = [
    "potential",
    "applied",
    "in_progress",
    "final_stage",
    "hired",
    "rejected",
    "withdrawn",
]


@pytest.mark.parametrize("status", VALID_STATUSES)
def test_verify_user_can_create_application_with_status(status):
    """Verify an application can be created with each valid status."""
    api_client = APIClient()

    payload = build_create_application_payload(status=status)
    application = create_application(api_client, payload=payload)

    assert application["status"] == status, (
        f"Expected status '{status}' but got '{application['status']}'"
    )

    delete_application(api_client, application["id"])