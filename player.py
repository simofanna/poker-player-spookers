from Random import randint


class Player:
    VERSION = "8"

    def betRequest(self, game_state): 
        return randint(150,1000)

    def showdown(self, game_state):
        pass

