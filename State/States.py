from State import State

# decorator
def singleton(cls, *args, **kwargs):
    "decorator function"
    instance = {}
    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton

@singleton
class SolidState(State):
    """Solid class"""

    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo < 0

    def behavior(self, context):
        print("Current state info:", context._getStateInfo())

@singleton
class LiquidState(State):
    """Liquid class"""

    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo >= 0 and stateInfo < 100

    def behavior(self, context):
        print("Current state info:", context._getStateInfo())

@singleton
class GaseousState(State):
    """Gaseous class"""

    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo >= 100

    def behavior(self, context):
        print("Current state info:", context._getStateInfo())