from dataclasses import dataclass

from backend.ConfigService import ConfigService
from backend.utils.TimeUtil import TimeUtil


@dataclass
class RadioState:
    frequency: int
    mode: str
    power: int
    is_transmitting: bool
    last_updated: str


class AbstractRadioControlService:

    def __init__(self, config_service: ConfigService):
        assert self._startup_test()
        self._config_service: ConfigService = config_service
        print("- RadioControlService initialized.")

    def get_state(self) -> RadioState:
        raise NotImplementedError("Method must be implemented in derived classes.")

    def set_frequency(self, frequency: int):
        raise NotImplementedError("Method must be implemented in derived classes.")

    def set_power(self, power: int):
        raise NotImplementedError("Method must be implemented in derived classes.")

    def set_mode(self, mode: str):
        raise NotImplementedError("Method must be implemented in derived classes.")

    def start_transmit(self):
        raise NotImplementedError("Method must be implemented in derived classes.")

    def stop_transmit(self):
        raise NotImplementedError("Method must be implemented in derived classes.")

    @staticmethod
    def _startup_test() -> bool:
        raise NotImplementedError("Method must be implemented in derived classes.")
