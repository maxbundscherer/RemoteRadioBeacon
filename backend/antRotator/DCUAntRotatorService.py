import asyncio
import os
import random
import time
from concurrent.futures import ThreadPoolExecutor

from backend.antRotator.AbstractAntRotatorService import AbstractAntRotatorService, AntRotatorState
from backend.utils.TimeUtil import TimeUtil


class DCUAntRotatorService(AbstractAntRotatorService):

    def __init__(self, config_service):
        self._is_busy: bool = False
        self._executor = ThreadPoolExecutor()
        super().__init__(config_service)

    @staticmethod
    def _startup_test() -> bool:
        # Check if rotctl is installed
        return os.system("rotctl -V") == 0

    async def _impl_async_update(self):

        output = os.popen("rotctl -m 406 -r /dev/ttyUSB0 p").read()

        print("OUTPUT: ", output)

        time.sleep(10)

        self._state = AntRotatorState(
            azimuth=round(random.uniform(0, 360), 2),
            elevation=round(random.uniform(0, 90), 2),
            last_updated=TimeUtil.get_current_time_utc_str()
        )

        self._is_busy = False

    def _start_async_update(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._impl_async_update())
        loop.close()

    def _trigger_update_state(self):
        if self._is_busy:
            print("WARNING: DCUAntRotatorService._trigger_update_state() called while busy. Ignoring.")
            return

        self._is_busy = True
        self._executor.submit(self._start_async_update)

    def set_azimuth(self, azimuth: float):
        if self._is_busy:
            print("WARNING: DCUAntRotatorService.set_azimuth() called while busy. Ignoring.")
            return

        print("WARNING: DummyAntRotatorService.set_azimuth() called. Ignoring.")
        print("SHOULD SET AZIMUTH TO: ", azimuth)

    def set_elevation(self, elevation: float):
        if self._is_busy:
            print("WARNING: DCUAntRotatorService.set_elevation() called while busy. Ignoring.")
            return

        pass
