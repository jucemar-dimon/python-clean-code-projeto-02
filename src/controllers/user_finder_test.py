from src.models.entities.users import Users
from .user_finder import UserFinder
import pytest


class UserRepositoryMock:
    def __init__(self):
        self.select_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return [Users(id=123, person_name="mocked_person", age=33, height=1.86)]


class UserRepositoryMockWithError:
    def __init__(self):
        self.select_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return []


def test_find_by_person_name():
    person_name = "my_person_name"
    user_repo = UserRepositoryMock()
    user_finder = UserFinder(user_repo)

    response = user_finder.find_by_person_name(person_name)

    assert user_repo.select_user_att["person_name"] == person_name
    assert isinstance(response, dict)
    assert response["Type"] == "Users"
    assert "attributes" in response
    assert isinstance(response["attributes"], list)


def test_find_by_person_name_with_error():
    user_repo = UserRepositoryMockWithError()
    user_finder = UserFinder(user_repo)
    with pytest.raises(Exception) as exc_info:
        user_finder.find_by_person_name("something")
    assert str(exc_info.value) == "Usuario nao encontrado!"
