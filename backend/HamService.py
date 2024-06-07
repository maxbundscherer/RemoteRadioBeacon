from backend.antRotator.AbstractAntRotatorService import AbstractAntRotatorService
from backend.antRotator.DummyAntRotatorService import DummyAntRotatorService
from backend.radioControl.AbstractRadioControlService import AbstractRadioControlService
from backend.radioControl.DummyRadioControlService import DummyRadioControlService


class HamService:

    def __init__(self):
        self._ant_rotator_service: AbstractAntRotatorService = DummyAntRotatorService()
        self._radio_control_service: AbstractRadioControlService = DummyRadioControlService()

        self._ant_rotator_service.test()
        self._radio_control_service.test()

        print("- HamService initialized.")
