import httpx
import faker


def create_user_data():
    fake = faker.Faker("ru_RU")
    return {
        "email": fake.email(),
        "password": fake.password(),
        "lastName": fake.last_name(),
        "firstName": fake.first_name(),
        "middleName": fake.middle_name()
    }


def update_user_data():
    data = create_user_data()
    del data["password"]
    return data


base_url = "http://localhost:8000"


# Create user
user_data = create_user_data()
response = httpx.post(
    url=base_url + "/api/v1/users",
    json=user_data
)
response.raise_for_status()
user_id = response.json()["user"]["id"]

# Login user
response = httpx.post(
    url=base_url + "/api/v1/authentication/login",
    json={"email": user_data["email"], "password": user_data["password"]}
)
response.raise_for_status()
access_token = response.json()["token"]["accessToken"]

# Update user
httpx.patch(
    url=base_url + f"/api/v1/users/{user_id}",
    headers={"Authorization": f"Bearer {access_token}"},
    json=update_user_data()
)
response.raise_for_status()
