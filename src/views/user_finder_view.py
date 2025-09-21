from src.controllers.interfaces.user_finder import UserFinderInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import handle_errors


class UserFinderView:
    def __init__(self, controller: UserFinderInterface):
        self.__controller = controller

    def handle_find_by_person_name(self, req: HttpRequest) -> HttpResponse:
        try:
            person_name = req.param["person_name"]
            response = self.__controller.find_by_person_name(person_name)
            return HttpResponse(status_code=200, body=response)
        except Exception as exception:
            return handle_errors(exception)
