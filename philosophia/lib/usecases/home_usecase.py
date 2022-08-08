import json

from philosophia.lib.dto.dto_encoder import DTOEncoder
from philosophia.lib.dto.usecases.home_usecase_request_dto import HomeUseCaseRequestDTO
from philosophia.lib.interfaces.repositories.philosophia_repo import IPhilosophiaRepo
from philosophia.lib.interfaces.usecases.usecase import Usecase


class HomeUseCase(Usecase):
    def __init__(self, repo: IPhilosophiaRepo):
        self.repo = repo

    def handle(self, request: HomeUseCaseRequestDTO):
        rooms = self.repo.load_all_rooms()
        user = self.repo.load_current_user(username=request.username)
        debates = self.repo.load_recent_debates()
        references = self.repo.load_top_references()
        return json.dumps({
            "user":
                json.loads(DTOEncoder().encode(user)),
            "rooms": json.loads(DTOEncoder().encode(rooms)),
            "debates": json.loads(DTOEncoder().encode(debates)),
            "references": json.loads(DTOEncoder().encode(references)),

        }, separators=(',', ':')
        )
