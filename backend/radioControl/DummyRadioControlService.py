from backend.radioControl.AbstractRadioControlService import AbstractRadioControlService, RadioState


class DummyRadioControlService(AbstractRadioControlService):

    def startup_test(self):
        pass

    def get_state(self) -> RadioState:
        return self._state
