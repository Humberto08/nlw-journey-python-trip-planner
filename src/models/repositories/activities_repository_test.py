from datetime import datetime
import pytest 
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .activities_repository import ActivitiesRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_registry_activity():
    conn = db_connection_handler.get_connection()
    activities_repository =ActivitiesRepository(conn)

    activity_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "title": "Viajar a Grecia",
        "occurs_at": datetime.now()
    }

    activities_repository.registry_activity(activity_infos)

@pytest.mark.skip(reason="interacao com o banco de dados")
def find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activities = activities_repository.find_activities_from_trip(trip_id)
    print()
    print(activities)
