import random

from backend.radioControl.AbstractRadioControlService import AbstractRadioControlService, RadioState
from backend.utils.TimeUtil import TimeUtil


class DummyRadioControlService(AbstractRadioControlService):

    @staticmethod
    def _startup_test() -> bool:
        return True

    def _trigger_update_state(self):
        self._state = RadioState(
            frequency=int(random.uniform(430e6, 440e6)),
            power=int(random.uniform(0, 100)),
            mode=['LSB', 'USB', 'CW', 'AM', 'FM'][random.randint(0, 4)],
            is_transmitting=random.choice([True, False]),
            last_updated=TimeUtil.get_current_time_utc_str()
        )
