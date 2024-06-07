import random

from backend.radioControl.AbstractRadioControlService import AbstractRadioControlService, RadioState
from backend.utils.TimeUtil import TimeUtil


class DummyRadioControlService(AbstractRadioControlService):

    @staticmethod
    def _startup_test() -> bool:
        return True

    def _trigger_update_state(self):
        self._state = RadioState(
            frequency=random.uniform(0, 1500),
            mode=['LSB', 'USB', 'CW', 'AM', 'FM', 'N/A'][random.randint(0, 5)],
            is_transmitting=random.choice([True, False]),
            last_updated=TimeUtil.get_current_time_utc_str()
        )
