from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface


class UserCreator:
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repo = users_repository
