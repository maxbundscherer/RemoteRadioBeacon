import asyncio
import os
import random
from concurrent.futures import ThreadPoolExecutor

from backend.radioControl.AbstractRadioControlService import AbstractRadioControlService, RadioState
from backend.utils.TimeUtil import TimeUtil


class KenwoodRadioControlService(AbstractRadioControlService):

    def __init__(self, config_service):
        self._is_busy: bool = False
        self._executor = ThreadPoolExecutor()
        super().__init__(config_service)

    @staticmethod
    def _startup_test() -> bool:
        # TODO
        return True

    async def _impl_async_update(self):

        # output = os.popen("rotctl -m 406 -r /dev/ttyUSB0 p").read()
        # lines = output.split("\n")
        #
        # if len(lines) == 3:
        #     line = lines[0]
        #     azimuth = float(line.split(" ")[0])
        #
        #     self._state = RadioState(
        #         frequency=int(random.uniform(430e6, 440e6)),
        #         power=int(random.uniform(0, 100)),
        #         mode=['LSB', 'USB', 'CW', 'AM', 'FM'][random.randint(0, 4)],
        #         is_transmitting=random.choice([True, False]),
        #         last_updated=TimeUtil.get_current_time_utc_str()
        #     )
        # else:
        #     print("WARNING: DCUAntRotatorService._impl_async_update() received unexpected output.")

        self._is_busy = False

    def _start_async_update(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._impl_async_update())
        loop.close()

    def _trigger_update_state(self):
        if self._is_busy:
            print("WARNING: KenwoodRadioControlService._trigger_update_state() called while busy. Ignoring.")
            return

        self._is_busy = True
        self._executor.submit(self._start_async_update)

    def set_frequency(self, frequency: int):
        if self._is_busy:
            print("WARNING: KenwoodRadioControlService.set_frequency() called while busy. Ignoring.")
            return
        # TODO
        print("WARNING: DummyRadioControlService.set_frequency() called. Ignoring.")
        print("SHOULD SET FREQUENCY TO", frequency)

    def set_power(self, power: int):
        if self._is_busy:
            print("WARNING: KenwoodRadioControlService.set_power() called while busy. Ignoring.")
            return
        # TODO
        print("WARNING: DummyRadioControlService.set_power() called. Ignoring.")
        print("SHOULD SET POWER TO", power)

    def set_mode(self, mode: str):
        if self._is_busy:
            print("WARNING: KenwoodRadioControlService.set_mode() called while busy. Ignoring.")
            return
        # TODO
        print("WARNING: DummyRadioControlService.set_mode() called. Ignoring.")
        print("SHOULD SET MODE TO", mode)

    def start_transmit(self):
        if self._is_busy:
            print("WARNING: KenwoodRadioControlService.start_transmit() called while busy. Ignoring.")
            return
        # TODO
        print("WARNING: DummyRadioControlService.start_transmit() called. Ignoring.")
        print("SHOULD START TRANSMITTING")
        print("WAV DURATION", self._config_service.get_local_wav_tx_duration())

    def stop_transmit(self):
        if self._is_busy:
            print("WARNING: KenwoodRadioControlService.stop_transmit() called while busy. Ignoring.")
            return
        # TODO
        print("WARNING: DummyRadioControlService.stop_transmit() called. Ignoring.")
        print("SHOULD STOP TRANSMITTING")
