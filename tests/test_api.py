import pytest
from datetime import datetime, timedelta
from unittest.mock import patch
from requests.exceptions import HTTPError
from python_everhour.api import EverhourAPI
import os


# Optional pytest marker to group tests
# pytestmark = pytest.mark.api

@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["X-Api-Key"]}

@pytest.fixture
def api_key():
    """Fixture to provide a mock API key."""
    return os.environ['EVERHOUR_API_KEY']


@pytest.fixture
def everhour_api(api_key):
    """Fixture to create an EverhourAPI instance with the mock key."""
    return EverhourAPI(api_key)


@pytest.mark.vcr
def test_get_time_entries(everhour_api):
    start_date = datetime.today() - timedelta(days=7)
    end_date = datetime.today()
    response = everhour_api.get_time_entries(start_date, end_date)
    assert response == "mock_time_entries_data"
    # mock_query.assert_called_once_with(
    #    f"/team/time?from={start_date.strftime('%Y-%m-%d')}&to={end_date.strftime('%Y-%m-%d')}"
    # )

@pytest.mark.vcr
def test_get_users(everhour_api):
    response = everhour_api.get_users()
    assert response is not None
    assert response == ""

#
# @patch("requests.get")
# def test_query_everhour_failure(mock_get, everhour_api):
#     mock_get.side_effect = HTTPError("API Error")
#     with pytest.raises(HTTPError):
#         everhour_api.query_everhour("/test_endpoint")
#

#
# def test_get_users(everhour_api):
#     """Test fetching users from Everhour API."""
#     # Mock response or use a fixture with known data
#     with patch("everhour_api.EverhourAPI.query_everhour") as mock_query:
#         mock_query.return_value = "mock_users_data"
#         response = everhour_api.get_users()
#         assert response == "mock_users_data"
#         mock_query.assert_called_once_with("/team/users")
#     # ... other tests
#
# def test_get_schedule_assignments(everhour_api):
#     """Test fetching schedule assignments from Everhour API."""
#     # Mock response or use a fixture with known data
#     with patch("everhour_api.EverhourAPI.query_everhour") as mock_query:
#         mock_query.return_value = "mock_schedule_assignments_data"
#         response = everhour_api.get_schedule_assignments()
#         assert response == "mock_schedule_assignments_data"
#         mock_query.assert_called_once_with("/resource-planner/assignments")
