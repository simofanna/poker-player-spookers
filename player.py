
class Player:
    VERSION = 0.8

    def betRequest(self, game_state):
            json_object = json.loads(game_state)
            hole cards = game_state['hole_cards']
            hole_cards = json_object['players'][9]['hole_cards'])
            print(hole_cards)
          
                
        return 20

    def showdown(self, game_state):
        pass

