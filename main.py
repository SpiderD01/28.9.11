import pytest
import requests

from pydantic import BaseModel

class AccessTokenRequest(BaseModel):
    access_token: abc

class User(BaseModel):
    id: 000
    first_name: cba
    last_name: xyz

def test_access_token_required():
    request = {
        "access_token": "token123"
    }
    AccessTokenRequest(**request)

def test_users_get_response():
    response = [
        {"id": 123, "first_name": "Ivan", "last_name": "Ivanov"},
        {"id": 456, "first_name": "Nikita", "last_name": "Nikitin"}
    ]
    users = [User(**user) for user in response]

def test_access_token_required():
    request = {}
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)


def test_access_token_format():
    request = {
        "access_token": "invalid_token_format"
    }
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)

def test_users_get_success():
    response = [
        {"id": 123, "first_name": "Ivan", "last_name": "Ivanov"},
        {"id": 456, "first_name": "Nikita", "last_name": "Nikitin"}
    ]
    users = [User(**user) for user in response]
    assert len(users) == 2
    assert users[0].id == 123
    assert users[0].first_name == "Ivan"
    assert users[0].last_name == "Ivanov"

def test_users_get_no_users():
    response = []
    users = [User(**user) for user in response]
    assert len(users) == 0

def test_user_format():
    user = {
        "id": "invalid_id_format",
        "first_name": "Ivan",
        "last_name": "Ivanov"
    }
    with pytest.raises(ValueError):
        User(**user)

def test_user_name_format():
    user = {
        "id": 123,
        "first_name": "2355Drew",
        "last_name": "Ivanov"
    }
    with pytest.raises(ValueError):
        User(**user)

def test_user_lastname_format():
    user = {
        "id": 321,
        "first_name": "Ivan",
        "last_name": "2354Drew"
    }
    with pytest.raises(ValueError):
        User(**user)
