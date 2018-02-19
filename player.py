from random import randint


class Player:
    VERSION = "8"

    def betRequest(self, game_state): 
        return randint(50,200)

    def showdown(self, game_state):
        pass

