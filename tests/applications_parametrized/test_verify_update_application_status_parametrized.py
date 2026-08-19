"""
Parametrized tests for updating application status through the PATCH endpoint.
"""

import pytest

from clients.api_client import APIClient
from helpers.application_helper import build_create_application_payload
from helpers.application_helper import create_application
from helpers.application_helper import delete_application
from helpers.application_helper import get_application

TRANSITION_STATUSES = [
    "applied",
    "in_progress",
    "final_stage",
    "hired",
    "rejected",
    "withdrawn",
]


@pytest.mark.parametrize("new_status", TRANSITION_STATUSES)
def test_verify_user_can_update_application_status_from_potential(new_status):
    """Verify an application status can be updated from potential to each valid status."""
    api_client = APIClient()

    payload = build_create_application_payload(status="potential")
    application = create_application(api_client, payload=payload)
    application_id = application["id"]

    update_endpoint = f"/api/v1/applications/{application_id}"
    update_payload = {"status": new_status}
    api_client.patch_json(update_endpoint, update_payload)

    updated = get_application(api_client, application_id)
    assert updated["status"] == new_status, (
        f"Expected status '{new_status}' after update but got '{updated['status']}'"
    )

    delete_application(api_client, application_id)