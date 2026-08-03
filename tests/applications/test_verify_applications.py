import requests
from configs.settings import BASE_URL


def test_verify_authenticated_user_can_get_applications():
    """
    This test intentionally does the login/token setup directly in the test.
    We will refactor this later after the repetition becomes obvious.
    """
    # Login first to get an access token
    login_url = f"{BASE_URL}/api/v1/auth/login"
    login_payload = {
        "email": "student@example.com",
        "password": "Password123!"
        }
    login_response = requests.post(login_url, json=login_payload)
    assert login_response.status_code == 200, f"Expected status code 200, but got {login_response.status_code}"

    access_token = login_response.json()["access_token"]

    # Use the token to call a protected endpoint
    url = f"{BASE_URL}/api/v1/applications"
    headers = {
        "Authorization": f"Bearer {access_token}"
        }
    response = requests.get(url, headers=headers)

    # Verify the response code
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Verify the response body
    response_body = response.json()
    assert isinstance(response_body, list), f"Expected response body to be a list but got {type(response_body)}"
    assert len(response_body) > 0, "Expected at least one application in the response"

    first_application = response_body[0]
    assert first_application["id"], f"Application id is required, but got {first_application['id']}"
    assert first_application["company_name"], f"Company name is required, but got {first_application['company_name']}"
    assert first_application["role_title"], f"Role title is required, but got {first_application['role_title']}"
    assert first_application["status"], f"Status is required, but got {first_application['status']}"


def test_verify_authenticated_user_can_get_application_summary():
    """
    This test repeats the login/token/header setup on purpose.
    The duplication will help us decide what to refactor next.
    """
    # Login first to get an access token
    login_url = f"{BASE_URL}/api/v1/auth/login"
    login_payload = {
        "email": "student@example.com",
        "password": "Password123!"
        }
    login_response = requests.post(login_url, json=login_payload)
    assert login_response.status_code == 200, f"Expected status code 200, but got {login_response.status_code}"

    access_token = login_response.json()["access_token"]

    # Use the token to call a protected endpoint
    url = f"{BASE_URL}/api/v1/applications/summary"
    headers = {
        "Authorization": f"Bearer {access_token}"
        }
    response = requests.get(url, headers=headers)

    # Verify the response code
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Verify the response body
    response_body = response.json()
    assert response_body["potential"] == 2
    assert response_body["applied"] == 1
    assert response_body["in_progress"] == 1
    assert response_body["final_stage"] == 0
    assert response_body["hired"] == 0
    assert response_body["rejected"] == 0
    assert response_body["withdrawn"] == 0
    assert response_body["total"] == 4
