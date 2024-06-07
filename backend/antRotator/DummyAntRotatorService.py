import random

from backend.antRotator.AbstractAntRotatorService import AbstractAntRotatorService, AntRotatorState
from backend.utils.TimeUtil import TimeUtil


class DummyAntRotatorService(AbstractAntRotatorService):

    @staticmethod
    def _startup_test() -> bool:
        return True

    def _trigger_update_state(self):
        self._state = AntRotatorState(
            azimuth=random.uniform(0, 360),
            elevation=random.uniform(0, 90),
            last_updated=TimeUtil.get_current_time_utc_str()
        )
