from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface


class UserFinder:
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repo = users_repository

    def find_by_person_name(self, person_name: str) -> dict:
        selected_users = self.__select_and_validate_user(person_name)
        return self.__format_response(selected_users)

    def __select_and_validate_user(self, person_name: str) -> list:
        selected_users = self.__users_repo.select_user(person_name)
        if not selected_users or len(selected_users) == 0:
            raise Exception("Usuario nao encontrado!")
        return selected_users

    def __format_response(self, selected_users: list) -> list:
        formatted_users = []
        for users in selected_users:
            formatted_users.append(
                {"id": users.id, "person_name": users.person_name, "age": users.height}
            )

        return {
            "Type": "Users",
            "count": len(formatted_users),
            "attributes": formatted_users,
        }
