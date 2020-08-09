
class Player: # model of a player
    def __init__(self):
        self._username = ""
        self._password = ""

    def create(self,data):
        self._username=data[0]
        self._password=data[1]
