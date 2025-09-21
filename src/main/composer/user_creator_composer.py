from src.models.repositories.users_repository import UsersRepository
from src.controllers.user_creator import UserCreator
from src.views.user_creator_view import UserCreatorView
from src.models.connection.db_connection_handler import DbConnectionHandler


def user_creator_composer():
    conn = DbConnectionHandler()
    model = UsersRepository(conn)
    controller = UserCreator(model)
    view = UserCreatorView(controller)
    return view
