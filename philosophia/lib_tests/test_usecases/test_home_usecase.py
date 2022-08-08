from unittest import TestCase

from philosophia.lib.dto.debate import Debate
from philosophia.lib.dto.philosophia_user import PhilosophiaUser
from philosophia.lib.dto.room import Room
from philosophia.lib.dto.reference import Reference
from philosophia.lib.repositories.philosophia_repository import PhilosophiaRepositoryIMPL
from philosophia.lib.usecases.home_usecase import HomeUseCase
from unittest.mock import MagicMock
from .util_data import home_usecase_data
from ...lib.dto.usecases.home_usecase_request_dto import HomeUseCaseRequestDTO


def prepare_repo():
    repo = PhilosophiaRepositoryIMPL()

    repo.load_current_user = MagicMock(return_value=PhilosophiaUser(
        username='me', debates=[], observations=[], rooms=[]))

    repo.load_all_rooms = MagicMock(return_value=[Room(
        id='', name='My Room', debates=[], observations=[], ownerships=[])])

    repo.load_recent_debates = MagicMock(
        return_value=[Debate(id='', participants=[], time=45345624, topic="Some Topic")])

    repo.load_top_references = MagicMock(return_value=[Reference(id='', links=[], name='Some Book')])

    return repo


class TestHomeUseCase(TestCase):

    def test_handle(self):
        usecase = HomeUseCase(prepare_repo())
        result = usecase.handle(request=HomeUseCaseRequestDTO(username='me'))
        self.assertEqual(home_usecase_data.get_json_string(), result)
