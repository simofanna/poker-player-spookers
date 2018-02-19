
class Player:
    VERSION = "0.8"

    def betRequest(self, game_state):    
        holeCards = game_state["players"][VERSION]["hole_cards"]
        communityCards = game_state["players"][VERSION]["community_cards"]

        try:
            if hole_cards[VERSION][0]["suit"] == hole_cards[VERSION][1]["suit"] or hole_cards[VERSION][0]["rank"] == hole_cards[VERSION][1]["rank"]:
                return 25
            else: 
                return 10
        except ValueError:
            print(community_cards)
    
    return 10

    def showdown(self, game_state):
        pass

