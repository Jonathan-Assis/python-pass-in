import pytest
from src.models.settings.connection import db_connection_handler
from .attendees_repository import AttendeesRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_attendee():
    event_id = "meu-uuid"
    attendee = {
        "uuid": "meu-uuid-attende",
        "name": "Nome 2",
        "email": "email2@email.com",
        "event_id": event_id,
    }

    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendee)
    print(response)

#@pytest.mark.skip(reason="Não é necessário")
def test_get_attendee_badge_by_id():
    attend_id = "meu-uuid-attende"
    attendees_repository = AttendeesRepository()
    response = attendees_repository.get_attendee_badge_by_id(attend_id)

    print(response)
