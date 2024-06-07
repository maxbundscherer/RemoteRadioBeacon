from backend.ConfigService import ConfigService
from backend.antRotator.AbstractAntRotatorService import AbstractAntRotatorService, AntRotatorState
from backend.antRotator.DummyAntRotatorService import DummyAntRotatorService
from backend.radioControl.AbstractRadioControlService import AbstractRadioControlService, RadioState
from backend.radioControl.DummyRadioControlService import DummyRadioControlService


class HamService:

    def __init__(self, config_service: ConfigService):

        if config_service.get_config().ant_rotator_service == 'DummyService':
            self._ant_rotator_service: AbstractAntRotatorService = DummyAntRotatorService(config_service)
        else:
            raise Exception("Unknown AntRotatorService", config_service.get_config().ant_rotator_service)

        if config_service.get_config().radio_control_service == 'DummyService':
            self._radio_control_service: AbstractRadioControlService = DummyRadioControlService(config_service)
        else:
            raise Exception("Unknown RadioControlService", config_service.get_config().radio_control_service)

        print("- HamService initialized.")

    def get_ant_rotator_state(self) -> AntRotatorState:
        return self._ant_rotator_service.get_state()

    def set_ant_rotator_azimuth(self, azimuth: float):
        self._ant_rotator_service.set_azimuth(azimuth)

    def set_ant_rotator_elevation(self, elevation: float):
        self._ant_rotator_service.set_elevation(elevation)

    def get_radio_state(self) -> RadioState:
        return self._radio_control_service.get_state()

    def start_radio_tx(self):
        self._radio_control_service.start_transmit()

    def stop_radio_tx(self):
        self._radio_control_service.stop_transmit()
