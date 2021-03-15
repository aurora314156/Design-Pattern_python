from abc import ABCMeta

class Context(metaclass=ABCMeta):
    """State pattern context class"""

    def __init__(self):
        self.__states = []
        self.__curState = None
        # record current state info for change state.
        self.__stateInfo = 0

    def addState(self, state):
        if state not in self.__states:
            self.__states.append(state)

    def changeState(self, state):
        if state is None:
            return False
        if self.__curState is None:
            print("Initialize water as", state.getName(), 'state.')
        else:
            print("Transform", self.__curState.getName(), "into ", state.getName())
        self.__curState = state
        self.addState(state)
        return True

    def getState(self):
        return self.__curState

    def _setStateInfo(self, stateInfo):
        self.__stateInfo = stateInfo
        for state in self.__states:
            if state.isMatch(stateInfo):
                self.changeState(state)

    def _getStateInfo(self):
        return self.__stateInfo