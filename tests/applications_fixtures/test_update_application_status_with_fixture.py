"""
Application tests that combine fixtures with parametrization.
"""

import pytest


@pytest.mark.parametrize("new_status", ["in_progress", "final_stage", "hired"])
def test_verify_user_can_update_application_status(api_client, created_application, new_status):
    application_id = created_application["id"]
    payload = {"status": new_status}

    response_body = api_client.patch_json(
        f"/api/v1/applications/{application_id}",
        payload
    )

    assert response_body["id"] == application_id
    assert response_body["status"] == new_status
