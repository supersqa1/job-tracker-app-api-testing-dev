"""
Application tests that use the shared api_client fixture.
"""


def test_verify_authenticated_user_can_get_paginated_applications(api_client):
    response_body = api_client.get_json(
        "/api/v1/applications?paginated=true&limit=2&offset=0"
    )

    assert "items" in response_body
    assert "total" in response_body
    assert response_body["limit"] == 2
    assert response_body["offset"] == 0
    assert isinstance(response_body["items"], list)


def test_verify_authenticated_user_can_limit_paginated_applications(api_client):
    response_body = api_client.get_json(
        "/api/v1/applications?paginated=true&limit=1&offset=0"
    )

    assert response_body["limit"] == 1
    assert response_body["offset"] == 0
    assert len(response_body["items"]) <= 1
