from Context import Context
from States import SolidState
from States import LiquidState
from States import GaseousState
from State import State

class Water(Context):
    """Water (H2O)"""
    def __init__(self):
        super().__init__()
        self.addState(SolidState("Solid"))
        self.addState(LiquidState("Liquid"))
        self.addState(GaseousState("Gaseous"))
        self.setTemperature(25)

    def getTemperature(self):
        return self._getStateInfo()

    def setTemperature(self, temperature):
        self._setStateInfo(temperature)

    def riseTemperature(self, step):
        self.setTemperature(self.getTemperature() + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.getTemperature() - step)

    def behavior(self):
        state = self.getState()
        if isinstance(state, State):
            state.behavior(self)
        return state.getName()