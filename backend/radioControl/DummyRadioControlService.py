import random

from backend.radioControl.AbstractRadioControlService import AbstractRadioControlService, RadioState
from backend.utils.TimeUtil import TimeUtil


class DummyRadioControlService(AbstractRadioControlService):

    @staticmethod
    def _startup_test() -> bool:
        return True

    def get_state(self) -> RadioState:
        return RadioState(
            frequency=int(random.uniform(430e6, 440e6)),
            power=int(random.uniform(0, 100)),
            mode=['LSB', 'USB', 'CW', 'AM', 'FM'][random.randint(0, 4)],
            is_transmitting=random.choice([True, False]),
            last_updated=TimeUtil.get_current_time_utc_str()
        )

    def set_frequency(self, frequency: int):
        print("WARNING: DummyRadioControlService.set_frequency() called. Ignoring.")
        print("SHOULD SET FREQUENCY TO", frequency)

    def set_power(self, power: int):
        print("WARNING: DummyRadioControlService.set_power() called. Ignoring.")
        print("SHOULD SET POWER TO", power)

    def set_mode(self, mode: str):
        print("WARNING: DummyRadioControlService.set_mode() called. Ignoring.")
        print("SHOULD SET MODE TO", mode)

    def start_transmit(self):
        print("WARNING: DummyRadioControlService.start_transmit() called. Ignoring.")
        print("SHOULD START TRANSMITTING")
        print("WAV DURATION", self._config_service.get_local_wav_tx_duration())

    def stop_transmit(self):
        print("WARNING: DummyRadioControlService.stop_transmit() called. Ignoring.")
        print("SHOULD STOP TRANSMITTING")
