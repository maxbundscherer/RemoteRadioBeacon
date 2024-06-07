import random

from backend.antRotator.AbstractAntRotatorService import AbstractAntRotatorService, AntRotatorState


class DummyAntRotatorService(AbstractAntRotatorService):

    @staticmethod
    def _startup_test() -> bool:
        return True

    def _trigger_update_state(self):
        self._state = AntRotatorState(
            azimuth=random.uniform(0, 360),
            elevation=random.uniform(0, 90)
        )
