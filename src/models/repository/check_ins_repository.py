from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from src.models.entities.attendees import Attendees
from sqlalchemy.exc import IntegrityError, NoResultFound

class checkInRepository:
    def insert_attendee(self, attendee_id: str) -> str:
        with db_connection_handler as database:
            try:
                check_in = (
                    CheckIns(attendeeId=attendee_id)
                )
                database.session.add(check_in)
                database.session.commit()
                return attendee_id
            except IntegrityError:
                raise Exception("Check in já cadastrado!")
            except Exception as exception:
                database.session.rollback()
                raise exception