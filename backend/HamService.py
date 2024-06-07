from backend.antRotator.AbstractAntRotatorService import AbstractAntRotatorService, AntRotatorState
from backend.antRotator.DummyAntRotatorService import DummyAntRotatorService
from backend.radioControl.AbstractRadioControlService import AbstractRadioControlService, RadioState
from backend.radioControl.DummyRadioControlService import DummyRadioControlService


class HamService:

    def __init__(self):
        self._ant_rotator_service: AbstractAntRotatorService = DummyAntRotatorService()
        self._radio_control_service: AbstractRadioControlService = DummyRadioControlService()

        print("- HamService initialized.")

    def get_ant_rotator_state(self) -> AntRotatorState:
        return self._ant_rotator_service.get_state()

    def get_radio_state(self) -> RadioState:
        return self._radio_control_service.get_state()
