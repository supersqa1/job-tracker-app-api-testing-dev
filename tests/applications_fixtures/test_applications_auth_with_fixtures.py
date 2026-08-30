"""
Application tests that use authenticated and unauthenticated API client fixtures.
"""


def test_verify_applications_list_requires_authentication(unauthenticated_api_client):
    response = unauthenticated_api_client.get(
        "/api/v1/applications",
        expected_status_code=401
    )

    response_body = response.json()
    assert response_body["error"]["code"] == "AUTHENTICATION_REQUIRED"
    assert response_body["error"]["message"] == "Authentication required"
