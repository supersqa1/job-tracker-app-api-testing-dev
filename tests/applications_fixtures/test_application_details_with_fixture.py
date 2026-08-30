"""
Application tests that use a fixture to create test data before the test runs.
"""


def test_verify_created_application_can_be_retrieved(api_client, created_application):
    application_id = created_application["id"]

    response_body = api_client.get_json(f"/api/v1/applications/{application_id}")

    assert response_body["id"] == application_id
    assert response_body["company_name"] == created_application["company_name"]
    assert response_body["role_title"] == created_application["role_title"]
