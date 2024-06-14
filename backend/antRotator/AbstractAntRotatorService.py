from dataclasses import dataclass

from backend.ConfigService import ConfigService
from backend.utils.TimeUtil import TimeUtil


@dataclass
class AntRotatorState:
    azimuth: float
    elevation: float
    last_updated: str


class AbstractAntRotatorService:

    def __init__(self, config_service: ConfigService):
        self._state: AntRotatorState = AntRotatorState(
            azimuth=-1,
            elevation=-1,
            last_updated="N/A"
        )
        assert self._startup_test()
        self._config_service: ConfigService = config_service
        print("- AntRotatorService initialized.")

    def get_state(self) -> AntRotatorState:
        self._trigger_update_state()
        return self._state

    def set_azimuth(self, azimuth: float):
        raise NotImplementedError("Method must be implemented in derived classes.")

    def set_elevation(self, elevation: float):
        raise NotImplementedError("Method must be implemented in derived classes.")

    @staticmethod
    def _startup_test() -> bool:
        raise NotImplementedError("Method must be implemented in derived classes.")

    def _trigger_update_state(self):
        raise NotImplementedError("Method must be implemented in derived classes.")
