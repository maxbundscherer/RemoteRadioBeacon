import asyncio
import os
import random
from concurrent.futures import ThreadPoolExecutor

from backend.ConfigService import ConfigService
from backend.radioControl.AbstractRadioControlService import AbstractRadioControlService, RadioState
from backend.utils.TimeUtil import TimeUtil


class KenwoodRadioControlService(AbstractRadioControlService):

    def __init__(self, config_service: ConfigService):
        self._is_transmitting: bool = False
        self._executor = ThreadPoolExecutor()
        self._config_service: ConfigService = config_service
        super().__init__(config_service)

    @staticmethod
    def _startup_test() -> bool:
        # Check if rotctl is installed
        return os.system("rigctl -V") == 0

    def get_state(self) -> RadioState:

        if self._is_transmitting:
            print("WARNING: KenwoodRadioControlService.get_state() called while transmitting. Ignoring.")
            return RadioState(
                frequency=-1,
                power=-1,
                mode="in_transmit",
                is_transmitting=self._is_transmitting,
                last_updated=TimeUtil.get_current_time_utc_str()
            )

        error_flag = False

        # print("Get Freq")
        r_freq: int = 0
        output = (os.popen(
            f'rigctl -m 2014 -s 38400 -r {self._config_service.get_config().radio_control_device} -P {self._config_service.get_config().radio_control_device} --set-conf=rts_state="OFF",dtr_state="OFF" get_freq')
                  .read()
                  ).split("\n")
        # print(f"Output [{len(output)}]  '{output}'")
        if len(output) == 3:
            r_freq: int = int(output[1])
            # print(f"Freq  '{r_freq}'")
        else:
            error_flag = True

        # print("Get Mode")
        r_mode: str = ""
        output = (os.popen(
            f'rigctl -m 2014 -s 38400 -r {self._config_service.get_config().radio_control_device} -P {self._config_service.get_config().radio_control_device} --set-conf=rts_state="OFF",dtr_state="OFF" get_mode')
                  .read()
                  ).split("\n")
        # print(f"Output [{len(output)}]  '{output}'")
        if len(output) == 4:
            r_mode: str = str(output[1])
            # print(f"Mode  '{r_mode}'")
        else:
            error_flag = True

        # print("Get Power")
        r_power: int = 0
        output = (os.popen(
            f'rigctl -m 2014 -s 38400 -r {self._config_service.get_config().radio_control_device} -P {self._config_service.get_config().radio_control_device} --set-conf=rts_state="OFF",dtr_state="OFF" get_level RFPOWER')
                  .read()
                  ).split("\n")
        # print(f"Output [{len(output)}]  '{output}'")
        if len(output) == 3:
            r_power: int = int(float(output[1]) * 100)
            # print(f"Power  '{r_power}'")
        else:
            error_flag = True

        if error_flag:
            return RadioState(
                frequency=-1,
                power=-1,
                mode="error",
                is_transmitting=self._is_transmitting,
                last_updated=TimeUtil.get_current_time_utc_str()
            )
        else:
            return RadioState(
                frequency=r_freq,
                power=r_power,
                mode=r_mode,
                is_transmitting=self._is_transmitting,
                last_updated=TimeUtil.get_current_time_utc_str()
            )

    # async def _impl_async_update(self):
    #
    #     # output = os.popen("rotctl -m 406 -r /dev/ttyUSB0 p").read()
    #     # lines = output.split("\n")
    #     #
    #     # if len(lines) == 3:
    #     #     line = lines[0]
    #     #     azimuth = float(line.split(" ")[0])
    #     #
    #     #     self._state = RadioState(
    #     #         frequency=int(random.uniform(430e6, 440e6)),
    #     #         power=int(random.uniform(0, 100)),
    #     #         mode=['LSB', 'USB', 'CW', 'AM', 'FM'][random.randint(0, 4)],
    #     #         is_transmitting=random.choice([True, False]),
    #     #         last_updated=TimeUtil.get_current_time_utc_str()
    #     #     )
    #     # else:
    #     #     print("WARNING: DCUAntRotatorService._impl_async_update() received unexpected output.")
    #
    #     self._is_busy = False
    #
    # def _start_async_update(self):
    #     loop = asyncio.new_event_loop()
    #     asyncio.set_event_loop(loop)
    #     loop.run_until_complete(self._impl_async_update())
    #     loop.close()
    #
    # def _trigger_update_state(self):
    #     if self._is_busy:
    #         print("WARNING: KenwoodRadioControlService._trigger_update_state() called while busy. Ignoring.")
    #         return
    #
    #     self._is_busy = True
    #     self._executor.submit(self._start_async_update)

    def set_frequency(self, frequency: int):
        if self._is_transmitting:
            print("WARNING: KenwoodRadioControlService.set_frequency() called while transmitting. Ignoring.")
            return
        # TODO
        print("WARNING: DummyRadioControlService.set_frequency() called. Ignoring.")
        print("SHOULD SET FREQUENCY TO", frequency)

    def set_power(self, power: int):
        if self._is_transmitting:
            print("WARNING: KenwoodRadioControlService.set_power() called while transmitting. Ignoring.")
            return
        # TODO
        print("WARNING: DummyRadioControlService.set_power() called. Ignoring.")
        print("SHOULD SET POWER TO", power)

    def set_mode(self, mode: str):
        if self._is_transmitting:
            print("WARNING: KenwoodRadioControlService.set_mode() called while transmitting. Ignoring.")
            return
        # TODO
        print("WARNING: DummyRadioControlService.set_mode() called. Ignoring.")
        print("SHOULD SET MODE TO", mode)

    def start_transmit(self):
        if self._is_transmitting:
            print("WARNING: KenwoodRadioControlService.start_transmit() called while transmitting. Ignoring.")
            return
        # TODO
        print("WARNING: DummyRadioControlService.start_transmit() called. Ignoring.")
        print("SHOULD START TRANSMITTING")
        print("WAV DURATION", self._config_service.get_local_wav_tx_duration())

    def stop_transmit(self):
        if self._is_transmitting:
            print("WARNING: KenwoodRadioControlService.stop_transmit() called while transmitting. Ignoring.")
            return
        # TODO
        print("WARNING: DummyRadioControlService.stop_transmit() called. Ignoring.")
        print("SHOULD STOP TRANSMITTING")
