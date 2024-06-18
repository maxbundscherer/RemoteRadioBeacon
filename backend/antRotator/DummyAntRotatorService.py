import random

from backend.antRotator.AbstractAntRotatorService import AbstractAntRotatorService, AntRotatorState
from backend.utils.TimeUtil import TimeUtil


class DummyAntRotatorService(AbstractAntRotatorService):

    @staticmethod
    def _startup_test() -> bool:
        return True

    def get_state(self) -> AntRotatorState:
        return AntRotatorState(
            azimuth=round(random.uniform(0, 360), 2),
            elevation=round(random.uniform(0, 90), 2),
            last_updated=TimeUtil.get_current_time_utc_str()
        )

    def set_azimuth(self, azimuth: float):
        print("WARNING: DummyAntRotatorService.set_azimuth() called. Ignoring.")
        print("SHOULD SET AZIMUTH TO: ", azimuth)

    def set_elevation(self, elevation: float):
        print("WARNING: DummyAntRotatorService.set_elevation() called. Ignoring.")
        print("SHOULD SET ELEVATION TO: ", elevation)
