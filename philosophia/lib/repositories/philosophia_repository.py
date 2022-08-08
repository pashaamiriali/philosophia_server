from philosophia.lib.dto.philosophia_user import PhilosophiaUser
from philosophia.lib.interfaces.repositories.philosophia_repo import IPhilosophiaRepo
from philosophia.models import RoomModel


class PhilosophiaRepositoryIMPL(IPhilosophiaRepo):

    def load_current_user(self, username):
        return PhilosophiaUser(username=username, rooms=[], debates=[], observations=[])

    def load_all_rooms(self):
        return []

    def load_recent_debates(self):
        return []

    def load_top_references(self):
        return []
