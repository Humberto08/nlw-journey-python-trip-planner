from datetime import datetime, timedelta
import pytest
import uuid
from .participants_repository import ParticipantsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
id = str(uuid.uuid4())
emails_to_invite_id= str(uuid.uuid4())




@pytest.mark.skip(reason="interacao com o banco de dados")
def test_registry_participant():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participant_infos = {
        "id": id,
        "trip_id": trip_id,
        "emails_to_invite_id": emails_to_invite_id,
        "name": "Gilson",
    }

    participants_repository.registry_participant(participant_infos)


@pytest.mark.skip(reason="interacao com o banco de dados")
def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participants = participants_repository.find_participants_from_trip(trip_id)
    print()
    print(participants)


@pytest.mark.skip(reason="interacao com o banco de dados")
def test_update_participant_status():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participants_repository.update_participant_status(id)

