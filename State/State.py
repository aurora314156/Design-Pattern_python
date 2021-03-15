from abc import abstractmethod
class State:
    """State class"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def isMatch(self, stateInfo):
        "check state info is match on range or not"
        return False

    @abstractmethod
    def behavior(self, context):
        pass