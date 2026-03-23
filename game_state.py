class GameState:
    def __init__(self, ai_game):
        """ Initialize Statistics"""
        self.settings = ai_game.settings
        self.reset_states()

    def reset_states(self):
        """Initialize staistics that can change during the game"""
        self.ships_left = self.settings.ship_limit    