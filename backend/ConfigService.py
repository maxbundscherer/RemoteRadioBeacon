import os
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from backend.utils.TimeUtil import TimeUtil


class ConfigService:
    C_APP_TITLE = 'RemoteBeacon'
    C_APP_VERSION = '0.0.2'
    C_LOCAL_FILE = 'config.json'

    @staticmethod
    def get_app_title() -> str:
        return ConfigService.C_APP_TITLE

    @staticmethod
    def get_app_version() -> str:
        return ConfigService.C_APP_VERSION

    @dataclass_json
    @dataclass
    class Config:
        tx_locator: str
        ant_rotator_service: str
        radio_control_service: str

    # @staticmethod
    # def to_json_file(config: Config, fp: str):
    #     json_data = config.to_json()
    #     with open(fp, 'w') as f:
    #         f.write(json_data)

    @staticmethod
    def from_json_file(fp: str) -> Config:
        assert fp is not None
        assert os.path.exists(fp)
        with open(fp, 'r') as f:
            json_data = f.read()
            return ConfigService.Config.from_json(json_data)

    def __init__(self):
        self._config: ConfigService.Config = ConfigService.from_json_file(ConfigService.C_LOCAL_FILE)
        self._startup_time: str = TimeUtil.get_current_time_utc_str()
        print("- ConfigService initialized.")

    def get_config(self) -> Config:
        return self._config

    def get_startup_time(self) -> str:
        return self._startup_time

# if __name__ == '__main__':
#     # sample_config = ConfigService.Config(tx_locator='JN59')
#     # ConfigService.to_json_file(sample_config, ConfigService.C_LOCAL_FILE)
