import os

from backend.antRotator.AbstractAntRotatorService import AbstractAntRotatorService, AntRotatorState
from backend.utils.TimeUtil import TimeUtil


class DCUAntRotatorService(AbstractAntRotatorService):

    @staticmethod
    def _startup_test() -> bool:
        # Check if rotctl is installed
        return os.system("rotctl -V") == 0

    def get_state(self) -> AntRotatorState:
        output = os.popen("rotctl -m 406 -r /dev/ttyUSB0 p").read()
        lines = output.split("\n")

        if len(lines) == 3:
            line = lines[0]
            azimuth = float(line.split(" ")[0])

            return AntRotatorState(
                azimuth=azimuth,
                elevation=-1,
                last_updated=TimeUtil.get_current_time_utc_str()
            )
        else:
            print("WARNING: DCUAntRotatorService._impl_async_update() received unexpected output.")
            return AntRotatorState(
                azimuth=-1,
                elevation=-1,
                last_updated=TimeUtil.get_current_time_utc_str()
            )

    def set_azimuth(self, azimuth: float):
        os.system(f"rotctl -m 406 -r /dev/ttyUSB0 P {azimuth} 0")

    def set_elevation(self, elevation: float):
        print("WARNING: DCUAntRotatorService.set_elevation() not implemented.")
