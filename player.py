from random import randint

class Player:
    VERSION = "8"


    def firstBetIndex(ourHoleCards, betIndex):
        if bet_index == 0:
            if ourHoleCards[0]["rank"] == ourHoleCards[1]["rank"]:
                 return 800
            else:
                checkIfGotHighCards(ourHoleCard)


    def checkIfGotHighCards(ourHoleCards):

        if ("A" in ourHoleCards.values()) or ("K" in ourHoleCards.values()) or ("Q" in ourHoleCards.values()) ("J" in ourHoleCards.values()):
            return 400
        else:
            return 100

        

    def betRequest(self, game_state): 
        try:
            betIndex = game_state["bet_index"]
            players = game_state["players"]
            communityCards = game_state["community_cards"]

           
            for player in players:
                if player["name"] == "Spookers": 
                    ourHoleCards = player["hole_cards"]

            firstBetIndex(ourHoleCards, betIndex)


        except BaseException:
            print("Error rased , playes: " + players + "our hole cards: " + ourHoleCards)

        finally:
            return randint(20,100)

    def showdown(self, game_state):
        pass


    def checkFromSecondBet(communityCards, ourHoleCards):
        if ourHoleCards[0]["rank"] == ourHoleCards[1]["rank"]:
                for card in community_cards:
                    if (card["rank"] == ourHoleCards[0]["rank"]) or (card["rank"] == ourHoleCards[1]["rank"]):
                        return 10000
                    else:
                        return checkIfGotHighCards(ourHoleCards)
        return checkIfGotHighCards(ourHoleCards)