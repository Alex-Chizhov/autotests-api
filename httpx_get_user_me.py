import httpx


base_url = "http://localhost:8000"

response = httpx.post(
    url=base_url + "/api/v1/authentication/login",
    json={"email": "user@example.com", "password": "password"}
)
access_token = response.json()["token"]["accessToken"]

response = httpx.get(
    url=base_url + "/api/v1/users/me",
    headers={"Authorization": f"Bearer {access_token}"}
)
print(response.json())
print(response.status_code)
