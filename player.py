from random import randint

class Player:
    VERSION = "8"

    def betRequest(self, game_state): 
        try:
            players = game_state["players"]
            communityCards = game_state["community_cards"]

           
            for player in players:
                if player["name"] == "Spookers": 
                    ourHoleCards = player["hole_cards"]

                    
            if ourHoleCards[0]["rank"] == ourHoleCards[1]["rank"]:
                for card in community_cards:
                    if (card["rank"] == ourHoleCards[0]["rank"]) or (card["rank"] == ourHoleCards[1]["rank"]):
                        return 10000
                    else:
                        return 100
            return randint(80,1000)
             

        except BaseException:
            print("Error rased , playes: " + players + "our hole cards: " + ourHoleCards)

        finally:
            return randint(80,1000)

    def showdown(self, game_state):
        pass

