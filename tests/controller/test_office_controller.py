import random

from src.office.office_actions import OfficeActions
from src.office import office_controller
from tests.mock_request import mock_request
import tests.mock_auth_controller
import tests.mock_auth_privileges
import pytest


class TestOfficeController:
    def test_controllers_get_states(self, mocker):
        states = office_controller.get_all_states()
        assert len(states) > 0
