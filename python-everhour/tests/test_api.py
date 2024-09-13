import os
from datetime import datetime, timedelta

import pytest

from python_everhour.api import EverhourAPI
from python_everhour import config

@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["X-Api-Key"]}


@pytest.fixture
def api_key():
    """Fixture to provide a mock API key."""
    return config.everhour.api_key 


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


@pytest.mark.vcr
def test_get_users(everhour_api):
    response = everhour_api.get_users()
    assert response is not None
    assert response == ""
