import asyncio
import os
import random
import time
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

    def set_frequency(self, frequency: int):
        if self._is_transmitting:
            print("WARNING: KenwoodRadioControlService.set_frequency() called while transmitting. Ignoring.")
            return
        os.popen(
            f'rigctl -m 2014 -s 38400 -r {self._config_service.get_config().radio_control_device} -P {self._config_service.get_config().radio_control_device} --set-conf=rts_state="OFF",dtr_state="OFF" set_freq {frequency}'
        ).read()

    def set_power(self, power: int):
        if self._is_transmitting:
            print("WARNING: KenwoodRadioControlService.set_power() called while transmitting. Ignoring.")
            return
        power_float = power / 100
        power_str = str(round(power_float, 2))
        os.popen(
            f'rigctl -m 2014 -s 38400 -r {self._config_service.get_config().radio_control_device} -P {self._config_service.get_config().radio_control_device} --set-conf=rts_state="OFF",dtr_state="OFF" set_level RFPOWER {power_str}'
        ).read()

    def set_mode(self, mode: str):
        if self._is_transmitting:
            print("WARNING: KenwoodRadioControlService.set_mode() called while transmitting. Ignoring.")
            return
        os.popen(
            f'rigctl -m 2014 -s 38400 -r {self._config_service.get_config().radio_control_device} -P {self._config_service.get_config().radio_control_device} --set-conf=rts_state="OFF",dtr_state="OFF" set_mode {mode} 0'
        ).read()

    async def _impl_async_tx(self):

        print("- [RADIO] Staring TX")

        print("- Radio Set PTT 1")
        os.popen(
            f'rigctl -m 2014 -s 38400 -r {self._config_service.get_config().radio_control_device} -P {self._config_service.get_config().radio_control_device} --set-conf=rts_state="ON",dtr_state="ON" T 1'
        ).read()

        # Start async aplay and play the wav file
        print("- [RADIO] Starting TX Audio")
        os.popen(
            f'aplay {self._config_service.C_LOCAL_WAV_TX_FILE}'
        )

        # Wait if process has finished
        has_fin = False
        while not has_fin:
            print("- [RADIO] Waiting for TX Audio to finish")
            output = (os.popen(
                f'ps -ef | grep aplay | grep -v grep')
                      .read())
            if output == "":
                has_fin = True
            else:
                time.sleep(1)

        print("- Radio Set PTT 0")
        os.popen(
            f'rigctl -m 2014 -s 38400 -r {self._config_service.get_config().radio_control_device} -P {self._config_service.get_config().radio_control_device} --set-conf=rts_state="OFF",dtr_state="OFF" T 0'
        ).read()

        print("- [RADIO] Finished TX")
        self._is_transmitting = False

    def _start_async_tx(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._impl_async_tx())
        loop.close()

    def _trigger_tx(self):
        self._is_transmitting = True
        self._executor.submit(self._start_async_tx)

    def start_transmit(self):
        if self._is_transmitting:
            print("WARNING: KenwoodRadioControlService.start_transmit() called while transmitting. Ignoring.")
            return
        self._trigger_tx()

    def stop_transmit(self):
        if not self._is_transmitting:
            print("WARNING: KenwoodRadioControlService.stop_transmit() called while not transmitting. Ignoring.")
            return
        os.popen(
            'pkill -i aplay'
        )
