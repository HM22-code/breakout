class State():
    """ State class for all states
    """
    
    def __init__(self, game):
        self.game = game
        
    def run(self):
        """ Called on every frames
        """
        pass
    
    def enter_state(self):
        """ Called when the state becomes the current state
        """
        pass
    
    def exit_state(self):
        """ Called when the state is no longer the current state
        """
        pass