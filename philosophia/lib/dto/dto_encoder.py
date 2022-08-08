from json import JSONEncoder


class DTOEncoder(JSONEncoder):
    def default(self, o) :
        return o.__dict__