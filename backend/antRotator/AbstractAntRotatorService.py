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
        assert self._startup_test()
        self._config_service: ConfigService = config_service
        print("- AntRotatorService initialized.")

    def get_state(self) -> AntRotatorState:
        raise NotImplementedError("Method must be implemented in derived classes.")

    def set_azimuth(self, azimuth: float):
        raise NotImplementedError("Method must be implemented in derived classes.")

    def set_elevation(self, elevation: float):
        raise NotImplementedError("Method must be implemented in derived classes.")

    @staticmethod
    def _startup_test() -> bool:
        raise NotImplementedError("Method must be implemented in derived classes.")
