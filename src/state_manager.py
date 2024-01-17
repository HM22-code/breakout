from states.start import Start

class StateManager():
    
    def __init__(self, display):
        self.current_state = Start(display, self)
        self.current_state.enter_state()
        self.previous_state = None
        
    def get_current_state(self):
        return self.current_state
    
    def get_previous_state(self):
        return self.previous_state
    
    def set_state(self, state):
        self.previous_state = self.current_state
        self.previous_state.exit_state()
        self.current_state = state
        self.current_state.enter_state()