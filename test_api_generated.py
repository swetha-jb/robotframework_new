import pytest
import requests

# ==================== GLOBAL CONFIGURATION ====================
BASE_URL = "https://ocapicep-internal-qa.netgear.com/api/v2"

# Common Headers (only headers that are IDENTICAL across all tests)
# Note: 'x-dreamfactory-api-key' and 'x-dreamfactory-session-token' are NOT common as they might change or be specific per test.
# However, 'Content-Type' is common in this dataset.
COMMON_HEADERS = {
    "Content-Type": "application/json"
}

# ==================== TEST FUNCTIONS ====================

def test_tc001_successful_user_registration():
    """
    Test ID: TC001
    Name: Successful User Registration
    Type: Positive
    Expected: 200 OK with user details
    """
    url = f"{BASE_URL}/ocRegister_MFA"

    headers = {
        "x-dreamfactory-api-key": "175208f843081dc7d9addad1e372c51c04c4c3dd54834a500d85955f71742a34",
        "x-dreamfactory-session-token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNlYXJjaGJsb3hAbmV0Z2Vhci5jb20iLCJleHAiOjE2OTE0NzgxNzQsImlhdCI6MTY5MTQ3Nzg3NH0.AYmd5-ya1OH6G-ap95Z2Ju_zCO8at2YRNxn62K5HfuplSfAdI1bJYUcRfH_GRtvIWcI8Ev2CEWaGYwKRFco21vYMeL9RsNkIG3eZx4w6b23El9stsBbAWbI7uj0UA5419_xmi miTza7U9HWEkhsfiprdu5H6FithbXx9t4YUGUj3uNC_mczEq-Kl_ZAeTp_075ArG3gGC7YjzHfa2pT2kp7gp4fIsp6saewvfjYeo6DKluW9PvkpWjHXW0aTLQTx3G7mnY42Z3vBApWJeBmYa5FHAgOsFN4bqSeGfjtCQecp2_K2j4WnKN2iKgxFrKS2Mi5H894-G1rhs7lMmxRQK1nj1ns_pRNKazXkJJAaPYTYIIskfHabjmD9lTpiCf3qNTeNiCQ_DqG59MbBs-TtIZuXGor-jZ1h9rEfaoVt3eF_2gz_PFJgkWSHtmJZWkYcYTNGv5v582hkSaz4g_09Sl3Zb0ICGxTf9eeGL6XEOEjhG3UjCcvm-5ddeemvYErt",
        **COMMON_HEADERS
    }
    payload = {
        "firstName": "fnamedemo",
        "lastName": "lnamedemo",
        "email": "aqdassss12s22@yopmail.com",
        "password": "Pass@1",
        "country": "IN",
        "language": "en",
        "phone": "1234567890",
        "address": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zipcode": "90210",
        "serialNumber": "SN123456789",
        "receiveCommunications": "0",
        "mailProgram": "1",
        "security_token": "sec_token_123",
        "acceptedPolicy": "true",
        "dateOfPurchase": "2023-01-01"
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_data = response.json()
    assert "meta" in response_data
    assert response_data["meta"]["code"] == 200
    assert "data" in response_data
    assert "token" in response_data["data"]
    assert "userId" in response_data["data"]
    assert "authenticated" in response_data["data"]
    assert "issued" in response_data["data"]
    assert "expiresIn" in response_data["data"]
    assert "mfa" in response_data["data"]
    assert "authCompleted" in response_data["data"]
    assert "MFA_State" in response_data["data"]
    assert "Customer_ID" in response_data["data"]
    assert "mailProgram" in response_data["data"]


def test_tc002_account_already_exists():
    """
    Test ID: TC002
    Name: Account Already Exists
    Type: Negative
    Expected: 400 Bad Request with error message
    """
    url = f"{BASE_URL}/ocRegister_MFA"

    headers = {
        "x-dreamfactory-api-key": "175208f843081dc7d9addad1e372c51c04c4c3dd54834a500d85955f71742a34",
        "x-dreamfactory-session-token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNlYXJjaGJsb3hAbmV0Z2Vhci5jb20iLCJleHAiOjE2OTE0NzgxNzQsImlhdCI6MTY5MTQ3Nzg3NH0.AYmd5-ya1OH6G-ap95Z2Ju_zCO8at2YRNxn62K5HfuplSfAdI1bJYUcRfH_GRtvIWcI8Ev2CEWaGYwKRFco21vYMeL9RsNkIG3eZx4w6b23El9stsBbAWbI7uj0UA5419_xmi miTza7U9HWEkhsfiprdu5H6FithbXx9t4YUGUj3uNC_mczEq-Kl_ZAeTp_075ArG3gGC7YjzHfa2pT2kp7gp4fIsp6saewvfjYeo6DKluW9PvkpWjHXW0aTLQTx3G7mnY42Z3vBApWJeBmYa5FHAgOsFN4bqSeGfjtCQecp2_K2j4WnKN2iKgxFrKS2Mi5H894-G1rhs7lMmxRQK1nj1ns_pRNKazXkJJAaPYTYIIskfHabjmD9lTpiCf3qNTeNiCQ_DqG59MbBs-TtIZuXGor-jZ1h9rEfaoVt3eF_2gz_PFJgkWSHtmJZWkYcYTNGv5v582hkSaz4g_09Sl3Zb0ICGxTf9eeGL6XEOEjhG3UjCcvm-5ddeemvYErt",
        **COMMON_HEADERS
    }
    payload = {
        "firstName": "existinguser",
        "lastName": "existinguser",
        "email": "existinguser@example.com",
        "password": "Password123",
        "country": "US",
        "receiveCommunications": "1"
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    response_data = response.json()
    assert "meta" in response_data
    assert response_data["meta"]["code"] == 400
    assert "error" in response_data["meta"]
    assert response_data["meta"]["error"] == 9013
    assert "message" in response_data["meta"]
    assert response_data["meta"]["message"] == "Account already exists"


def test_tc003_missing_required_field_email():
    """
    Test ID: TC003
    Name: Missing Required Field - Email
    Type: Negative
    Expected: 400 Bad Request with validation error for email
    """
    url = f"{BASE_URL}/ocRegister_MFA"

    headers = {
        "x-dreamfactory-api-key": "175208f843081dc7d9addad1e372c51c04c4c3dd54834a500d85955f71742a34",
        "x-dreamfactory-session-token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNlYXJjaGJsb3hAbmV0Z2Vhci5jb20iLCJleHAiOjE2OTE0NzgxNzQsImlhdCI6MTY5MTQ3Nzg3NH0.AYmd5-ya1OH6G-ap95Z2Ju_zCO8at2YRNxn62K5HfuplSfAdI1bJYUcRfH_GRtvIWcI8Ev2CEWaGYwKRFco21vYMeL9RsNkIG3eZx4w6b23El9stsBbAWbI7uj0UA5419_xmi miTza7U9HWEkhsfiprdu5H6FithbXx9t4YUGUj3uNC_mczEq-Kl_ZAeTp_075ArG3gGC7YjzHfa2pT2kp7gp4fIsp6saewvfjYeo6DKluW9PvkpWjHXW0aTLQTx3G7mnY42Z3vBApWJeBmYa5FHAgOsFN4bqSeGfjtCQecp2_K2j4WnKN2iKgxFrKS2Mi5H894-G1rhs7lMmxRQK1nj1ns_pRNKazXkJJAaPYTYIIskfHabjmD9lTpiCf3qNTeNiCQ_DqG59MbBs-TtIZuXGor-jZ1h9rEfaoVt3eF_2gz_PFJgkWSHtmJZWkYcYTNGv5v582hkSaz4g_09Sl3Zb0ICGxTf9eeGL6XEOEjhG3UjCcvm-5ddeemvYErt",
        **COMMON_HEADERS
    }
    payload = {
        "firstName": "test",
        "lastName": "user",
        "password": "Password123",
        "country": "US",
        "receiveCommunications": "1"
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    response_data = response.json()
    assert "meta" in response_data
    assert response_data["meta"]["code"] == 400
    assert "message" in response_data["meta"]
    assert response_data["meta"]["message"] == "Resource validation error"
    assert "validationErrors" in response_data["meta"]
    assert "items" in response_data["meta"]["validationErrors"]
    assert len(response_data["meta"]["validationErrors"]["items"]) > 0
    assert response_data["meta"]["validationErrors"]["items"][0]["propertyPath"] == "email"
    assert "Email is required" in response_data["meta"]["validationErrors"]["items"][0]["message"]


def test_tc004_invalid_email_format():
    """
    Test ID: TC004
    Name: Invalid Email Format
    Type: Negative
    Expected: 400 Bad Request with validation error for email format
    """
    url = f"{BASE_URL}/ocRegister_MFA"

    headers = {
        "x-dreamfactory-api-key": "175208f843081dc7d9addad1e372c51c04c4c3dd54834a500d85955f71742a34",
        "x-dreamfactory-session-token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNlYXJjaGJsb3hAbmV0Z2Vhci5jb20iLCJleHAiOjE2OTE0NzgxNzQsImlhdCI6MTY5MTQ3Nzg3NH0.AYmd5-ya1OH6G-ap95Z2Ju_zCO8at2YRNxn62K5HfuplSfAdI1bJYUcRfH_GRtvIWcI8Ev2CEWaGYwKRFco21vYMeL9RsNkIG3eZx4w6b23El9stsBbAWbI7uj0UA5419_xmi miTza7U9HWEkhsfiprdu5H6FithbXx9t4YUGUj3uNC_mczEq-Kl_ZAeTp_075ArG3gGC7YjzHfa2pT2kp7gp4fIsp6saewvfjYeo6DKluW9PvkpWjHXW0aTLQTx3G7mnY42Z3vBApWJeBmYa5FHAgOsFN4bqSeGfjtCQecp2_K2j4WnKN2iKgxFrKS2Mi5H894-G1rhs7lMmxRQK1nj1ns_pRNKazXkJJAaPYTYIIskfHabjmD9lTpiCf3qNTeNiCQ_DqG59MbBs-TtIZuXGor-jZ1h9rEfaoVt3eF_2gz_PFJgkWSHtmJZWkYcYTNGv5v582hkSaz4g_09Sl3Zb0ICGxTf9eeGL6XEOEjhG3UjCcvm-5ddeemvYErt",
        **COMMON_HEADERS
    }
    payload = {
        "firstName": "test",
        "lastName": "user",
        "email": "invalid-email",
        "password": "Password123",
        "country": "US",
        "receiveCommunications": "1"
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    response_data = response.json()
    assert "meta" in response_data
    assert response_data["meta"]["code"] == 400
    assert "message" in response_data["meta"]
    assert response_data["meta"]["message"] == "Resource validation error"
    assert "validationErrors" in response_data["meta"]
    assert "items" in response_data["meta"]["validationErrors"]
    assert len(response_data["meta"]["validationErrors"]["items"]) > 0
    assert response_data["meta"]["validationErrors"]["items"][0]["propertyPath"] == "email"
    assert "invalidValue" in response_data["meta"]["validationErrors"]["items"][0]
    assert response_data["meta"]["validationErrors"]["items"][0]["invalidValue"] == "invalid-email"
    assert "Email must be between 6-190 symbols in public email format" in response_data["meta"]["validationErrors"]["items"][0]["message"]


def test_tc005_invalid_password_format():
    """
    Test ID: TC005
    Name: Invalid Password Format
    Type: Negative
    Expected: 400 Bad Request with validation error for password format
    """
    url = f"{BASE_URL}/ocRegister_MFA"

    headers = {
        "x-dreamfactory-api-key": "175208f843081dc7d9addad1e372c51c04c4c3dd54834a500d85955f71742a34",
        "x-dreamfactory-session-token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNlYXJjaGJsb3hAbmV0Z2Vhci5jb20iLCJleHAiOjE2OTE0NzgxNzQsImlhdCI6MTY5MTQ3Nzg3NH0.AYmd5-ya1OH6G-ap95Z2Ju_zCO8at2YRNxn62K5HfuplSfAdI1bJYUcRfH_GRtvIWcI8Ev2CEWaGYwKRFco21vYMeL9RsNkIG3eZx4w6b23El9stsBbAWbI7uj0UA5419_xmi miTza7U9HWEkhsfiprdu5H6FithbXx9t4YUGUj3uNC_mczEq-Kl_ZAeTp_075ArG3gGC7YjzHfa2pT2kp7gp4fIsp6saewvfjYeo6DKluW9PvkpWjHXW0aTLQTx3G7mnY42Z3vBApWJeBmYa5FHAgOsFN4bqSeGfjtCQecp2_K2j4WnKN2iKgxFrKS2Mi5H894-G1rhs7lMmxRQK1nj1ns_pRNKazXkJJAaPYTYIIskfHabjmD9lTpiCf3qNTeNiCQ_DqG59MbBs-TtIZuXGor-jZ1h9rEfaoVt3eF_2gz_PFJgkWSHtmJZWkYcYTNGv5v582hkSaz4g_09Sl3Zb0ICGxTf9eeGL6XEOEjhG3UjCcvm-5ddeemvYErt",
        **COMMON_HEADERS
    }
    payload = {
        "firstName": "test",
        "lastName": "user",
        "email": "testuser@example.com",
        "password": "password",
        "country": "US",
        "receiveCommunications": "1"
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    response_data = response.json()
    assert "meta" in response_data
    assert response_data["meta"]["code"] == 400
    assert "message" in response_data["meta"]
    assert response_data["meta"]["message"] == "Resource validation error"
    assert "validationErrors" in response_data["meta"]
    assert "items" in response_data["meta"]["validationErrors"]
    assert len(response_data["meta"]["validationErrors"]["items"]) > 0
    assert response_data["meta"]["validationErrors"]["items"][0]["propertyPath"] == "password"
    assert "invalidValue" in response_data["meta"]["validationErrors"]["items"][0]
    assert response_data["meta"]["validationErrors"]["items"][0]["invalidValue"] == "password"
    assert "Password must contain at least one [0-9] digit; password must contain at least one [A-Z] character; password must contain at least one [a-z] character; password must be between 6-128 characters" in response_data["meta"]["validationErrors"]["items"][0]["message"]


def test_tc006_invalid_country_code():
    """
    Test ID: TC006
    Name: Invalid Country Code
    Type: Negative
    Expected: 400 Bad Request with validation error for country code
    """
    url = f"{BASE_URL}/ocRegister_MFA"

    headers = {
        "x-dreamfactory-api-key": "175208f843081dc7d9addad1e372c51c04c4c3dd54834a500d85955f71742a34",
        "x-dreamfactory-session-token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNlYXJjaGJsb3hAbmV0Z2Vhci5jb20iLCJleHAiOjE2OTE0NzgxNzQsImlhdCI6MTY5MTQ3Nzg3NH0.AYmd5-ya1OH6G-ap95Z2Ju_zCO8at2YRNxn62K5HfuplSfAdI1bJYUcRfH_GRtvIWcI8Ev2CEWaGYwKRFco21vYMeL9RsNkIG3eZx4w6b23El9stsBbAWbI7uj0UA5419_xmi miTza7U9HWEkhsfiprdu5H6FithbXx9t4YUGUj3uNC_mczEq-Kl_ZAeTp_075ArG3gGC7YjzHfa2pT2kp7gp4fIsp6saewvfjYeo6DKluW9PvkpWjHXW0aTLQTx3G7mnY42Z3vBApWJeBmYa5FHAgOsFN4bqSeGfjtCQecp2_K2j4WnKN2iKgxFrKS2Mi5H894-G1rhs7lMmxRQK1nj1ns_pRNKazXkJJAaPYTYIIskfHabjmD9lTpiCf3qNTeNiCQ_DqG59MbBs-TtIZuXGor-jZ1h9rEfaoVt3eF_2gz_PFJgkWSHtmJZWkYcYTNGv5v582hkSaz4g_09Sl3Zb0ICGxTf9eeGL6XEOEjhG3UjCcvm-5ddeemvYErt",
        **COMMON_HEADERS
    }
    payload = {
        "firstName": "test",
        "lastName": "user",
        "email": "testuser@example.com",
        "password": "Password123",
        "country": "INVALID",
        "receiveCommunications": "1"
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    response_data = response.json()
    assert "meta" in response_data
    assert response_data["meta"]["code"] == 400
    assert "message" in response_data["meta"]
    assert response_data["meta"]["message"] == "Resource validation error"
    assert "validationErrors" in response_data["meta"]
    assert "items" in response_data["meta"]["validationErrors"]
    assert len(response_data["meta"]["validationErrors"]["items"]) > 0
    assert response_data["meta"]["validationErrors"]["items"][0]["propertyPath"] == "country"
    assert "invalidValue" in response_data["meta"]["validationErrors"]["items"][0]
    assert response_data["meta"]["validationErrors"]["items"][0]["invalidValue"] == "INVALID"
    assert "two letter country code according to ISO 3166-2" in response_data["meta"]["validationErrors"]["items"][0]["message"]


def test_tc007_missing_required_field_lastname():
    """
    Test ID: TC007
    Name: Missing Required Field - LastName
    Type: Negative
    Expected: 400 Bad Request with validation error for lastName
    """
    url = f"{BASE_URL}/ocRegister_MFA"

    headers = {
        "x-dreamfactory-api-key": "175208f843081dc7d9addad1e372c51c04c4c3dd54834a500d85955f71742a34",
        "x-dreamfactory-session-token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNlYXJjaGJsb3hAbmV0Z2Vhci5jb20iLCJleHAiOjE2OTE0NzgxNzQsImlhdCI6MTY5MTQ3Nzg3NH0.AYmd5-ya1OH6G-ap95Z2Ju_zCO8at2YRNxn62K5HfuplSfAdI1bJYUcRfH_GRtvIWcI8Ev2CEWaGYwKRFco21vYMeL9RsNkIG3eZx4w6b23El9stsBbAWbI7uj0UA5419_xmi miTza7U9HWEkhsfiprdu5H6FithbXx9t4YUGUj3uNC_mczEq-Kl_ZAeTp_075ArG3gGC7YjzHfa2pT2kp7gp4fIsp6saewvfjYeo6DKluW9PvkpWjHXW0aTLQTx3G7mnY42Z3vBApWJeBmYa5FHAgOsFN4bqSeGfjtCQecp2_K2j4WnKN2iKgxFrKS2Mi5H894-G1rhs7lMmxRQK1nj1ns_pRNKazXkJJAaPYTYIIskfHabjmD9lTpiCf3qNTeNiCQ_DqG59MbBs-TtIZuXGor-jZ1h9rEfaoVt3eF_2gz_PFJgkWSHtmJZWkYcYTNGv5v582hkSaz4g_09Sl3Zb0ICGxTf9eeGL6XEOEjhG3UjCcvm-5ddeemvYErt",
        **COMMON_HEADERS
    }
    payload = {
        "firstName": "test",
        "email": "testuser@example.com",
        "password": "Password123",
        "country": "US",
        "receiveCommunications": "1"
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    response_data = response.json()
    assert "meta" in response_data
    assert response_data["meta"]["code"] == 400
    assert "message" in response_data["meta"]
    assert response_data["meta"]["message"] == "Resource validation error"
    assert "validationErrors" in response_data["meta"]
    assert "items" in response_data["meta"]["validationErrors"]
    assert len(response_data["meta"]["validationErrors"]["items"]) > 0
    assert response_data["meta"]["validationErrors"]["items"][0]["propertyPath"] == "lastName"
    assert "lastName must be between 1-64 symbols" in response_data["meta"]["validationErrors"]["items"][0]["message"]


def test_tc008_missing_required_field_firstname():
    """
    Test ID: TC008
    Name: Missing Required Field - FirstName
    Type: Negative
    Expected: 400 Bad Request with validation error for firstName
    """
    url = f"{BASE_URL}/ocRegister_MFA"

    headers = {
        "x-dreamfactory-api-key": "175208f843081dc7d9addad1e372c51c04c4c3dd54834a500d85955f71742a34",
        "x-dreamfactory-session-token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNlYXJjaGJsb3hAbmV0Z2Vhci5jb20iLCJleHAiOjE2OTE0NzgxNzQsImlhdCI6MTY5MTQ3Nzg3NH0.AYmd5-ya1OH6G-ap95Z2Ju_zCO8at2YRNxn62K5HfuplSfAdI1bJYUcRfH_GRtvIWcI8Ev2CEWaGYwKRFco21vYMeL9RsNkIG3eZx4w6b23El9stsBbAWbI7uj0UA5419_xmi miTza7U9HWEkhsfiprdu5H6FithbXx9t4YUGUj3uNC_mczEq-Kl_ZAeTp_075ArG3gGC7YjzHfa2pT2kp7gp4fIsp6saewvfjYeo6DKluW9PvkpWjHXW0aTLQTx3G7mnY42Z3vBApWJeBmYa5FHAgOsFN4bqSeGfjtCQecp2_K2j4WnKN2iKgxFrKS2Mi5H894-G1rhs7lMmxRQK1nj1ns_pRNKazXkJJAaPYTYIIskfHabjmD9lTpiCf3qNTeNiCQ_DqG59MbBs-TtIZuXGor-jZ1h9rEfaoVt3eF_2gz_PFJgkWSHtmJZWkYcYTNGv5v582hkSaz4g_09Sl3Zb0ICGxTf9eeGL6XEOEjhG3UjCcvm-5ddeemvYErt",
        **COMMON_HEADERS
    }
    payload = {
        "lastName": "user",
        "email": "testuser@example.com",
        "password": "Password123",
        "country": "US",
        "receiveCommunications": "1"
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    response_data = response.json()
    assert "meta" in response_data
    assert response_data["meta"]["code"] == 400
    assert "message" in response_data["meta"]
    assert response_data["meta"]["message"] == "Resource validation error"
    assert "validationErrors" in response_data["meta"]
    assert "items" in response_data["meta"]["validationErrors"]
    assert len(response_data["meta"]["validationErrors"]["items"]) > 0
    assert response_data["meta"]["validationErrors"]["items"][0]["propertyPath"] == "firstName"
    assert "firstName must be between 1-64 symbols" in response_data["meta"]["validationErrors"]["items"][0]["message"]


def test_tc009_missing_required_field_country():
    """
    Test ID: TC009
    Name: Missing Required Field - Country
    Type: Negative
    Expected: 400 Bad Request with validation error for country
    """
    url = f"{BASE_URL}/ocRegister_MFA"

    headers = {
        "x-dreamfactory-api-key": "175208f843081dc7d9addad1e372c51c04c4c3dd54834a500d85955f71742a34",
        "x-dreamfactory-session-token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNlYXJjaGJsb3hAbmV0Z2Vhci5jb20iLCJleHAiOjE2OTE0NzgxNzQsImlhdCI6MTY5MTQ3Nzg3NH0.AYmd5-ya1OH6G-ap95Z2Ju_zCO8at2YRNxn62K5HfuplSfAdI1bJYUcRfH_GRtvIWcI8Ev2CEWaGYwKRFco21vYMeL9RsNkIG3eZx4w6b23El9stsBbAWbI7uj0UA5419_xmi miTza7U9HWEkhsfiprdu5H6FithbXx9t4YUGUj3uNC_mczEq-Kl_ZAeTp_075ArG3gGC7YjzHfa2pT2kp7gp4fIsp6saewvfjYeo6DKluW9PvkpWjHXW0aTLQTx3G7mnY42Z3vBApWJeBmYa5FHAgOsFN4bqSeGfjtCQecp2_K2j4WnKN2iKgxFrKS2Mi5H894-G1rhs7lMmxRQK1nj1ns_pRNKazXkJJAaPYTYIIskfHabjmD9lTpiCf3qNTeNiCQ_DqG59MbBs-TtIZuXGor-jZ1h9rEfaoVt3eF_2gz_PFJgkWSHtmJZWkYcYTNGv5v582hkSaz4g_09Sl3Zb0ICGxTf9eeGL6XEOEjhG3UjCcvm-5ddeemvYErt",
        **COMMON_HEADERS
    }
    payload = {
        "firstName": "test",
        "lastName": "user",
        "email": "testuser@example.com",
        "password": "Password123",
        "receiveCommunications": "1"
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    response_data = response.json()
    assert "meta" in response_data
    assert response_data["meta"]["code"] == 400
    assert "message" in response_data["meta"]
    assert response_data["meta"]["message"] == "Resource validation error"
    assert "validationErrors" in response_data["meta"]
    assert "items" in response_data["meta"]["validationErrors"]
    assert len(response_data["meta"]["validationErrors"]["items"]) > 0
    assert response_data["meta"]["validationErrors"]["items"][0]["propertyPath"] == "country"
    assert "Country is required" in response_data["meta"]["validationErrors"]["items"][0]["message"]