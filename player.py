from random import randint

class Player:
    VERSION = "8"


    def firstBetIndex(ourHoleCards, betIndex, current_buy_in):
        if bet_index == 0:
            if ourHoleCards[0]["rank"] == ourHoleCards[1]["rank"]:
                 return 10000
            else:
                return checkIfGotHighCards(ourHoleCard, current_buy_in)


    def checkIfGotHighCards(ourHoleCards, current_buy_in):

        if ("A" in ourHoleCards.values()) or ("K" in ourHoleCards.values()) or ("Q" in ourHoleCards.values()) ("J" in ourHoleCards.values()):
            return current_buy_in
        else:
            return 0

    
    def betRequest(self, game_state): 
        try:
            betIndex = game_state["bet_index"]
            players = game_state["players"]
            communityCards = game_state["community_cards"]
            dealer = game_state["dealer"]
            current_buy_in = game_state["current_buy_in"]
            
           
            for player in players:
                if player["name"] == "Spookers": 
                    ourHoleCards = player["hole_cards"]
                    if player["id"] == (dealer+1) % (players.length) or player["id"] == (dealer+2) % (players.length):
                        if betIndex == 0:
                            if current_buy_in > player["bet"]:
                                if firstBetIndex(ourHoleCards, betIndex, current_buy_in) > 0:
                                    return (current_buy_in - player["bet"])
                    else:
                        return firstBetIndex(ourHoleCards, betIndex, current_buy_in)


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