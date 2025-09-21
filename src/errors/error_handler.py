from src.views.http_types.http_response import HttpResponse
from error_types.http_not_found import HttpNotFoundError
from error_types.http_bad_request import HttpBadRequestError


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpBadRequestError)):
        return HttpResponse(
            status_code=error.status_code,
            body={"erros"[{"title": error.name, "detail": error.message}]},
        )
    return HttpResponse(
        body={"erros"[{"title": "Server Error", "detail": str(error)}]},
    )
