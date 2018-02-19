from Random import randint


class Player:
    VERSION = "8"

    def betRequest(self, game_state): 
    try:
        players = game_state["players"]
            
            for player in players:
                if player["name"] = "Spookers": 
                    ourHoleCards = player["hole_cards"]
                    
            if ourHoleCards[0]["rank"] == ourHoleCards[1]["rank"]:
                return 100
            else: 
                return 20
    except BaseException:
        print("Error rased , playes: " + players + "our hole cards: " + ourHoleCards)

    finally:
        return randint(150,1000)

    def showdown(self, game_state):
        pass

