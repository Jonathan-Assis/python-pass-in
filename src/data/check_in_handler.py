from src.models.repository.check_ins_repository import CheckInRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class CheckInHandler:
    def __init__(self) -> None:
        self.__check_in_respository = CheckInRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        check_in = http_request.param["attendee_id"]
        self.__check_in_respository.insert_check_in(check_in)
    
        return HttpResponse(
            body=None,
            status_code=201
        )