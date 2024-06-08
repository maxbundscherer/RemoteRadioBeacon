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
        self._state: RadioState = RadioState(
            frequency=-1,
            mode='N/A',
            power=-1,
            is_transmitting=False,
            last_updated=TimeUtil.get_current_time_utc_str()
        )
        assert self._startup_test()
        self._config_service: ConfigService = config_service
        print("- RadioControlService initialized.")

    def get_state(self) -> RadioState:
        self._trigger_update_state()
        return self._state

    def set_frequency(self, frequency: int):
        raise NotImplementedError("Method must be implemented in derived classes.")

    def set_power(self, power: int):
        raise NotImplementedError("Method must be implemented in derived classes.")

    def start_transmit(self):
        raise NotImplementedError("Method must be implemented in derived classes.")

    def stop_transmit(self):
        raise NotImplementedError("Method must be implemented in derived classes.")

    @staticmethod
    def _startup_test() -> bool:
        raise NotImplementedError("Method must be implemented in derived classes.")

    def _trigger_update_state(self):
        raise NotImplementedError("Method must be implemented in derived classes.")
