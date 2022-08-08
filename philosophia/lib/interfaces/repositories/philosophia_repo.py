from abc import ABC, abstractmethod


class IPhilosophiaRepo(ABC):
    @abstractmethod
    def load_current_user(self, username):
        pass

    @abstractmethod
    def load_all_rooms(self):
        pass

    @abstractmethod
    def load_recent_debates(self):
        pass

    @abstractmethod
    def load_top_references(self):
        pass
