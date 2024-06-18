import os
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from backend.utils.TimeUtil import TimeUtil

import librosa


class ConfigService:
    C_APP_TITLE = 'RemoteRadioBeacon'
    C_APP_VERSION = '0.0.5'
    C_LOCAL_FILE = 'radioresources/config.json'

    C_LOCAL_WAV_TX_FILE = 'radioresources/transmit.wav'
    C_LOCAL_WAV_TX_SR = -1
    C_LOCAL_WAV_TX_DURATION = -1

    @staticmethod
    def get_app_title() -> str:
        return ConfigService.C_APP_TITLE

    @staticmethod
    def get_app_version() -> str:
        return ConfigService.C_APP_VERSION

    @staticmethod
    def get_local_wav_tx_sr() -> int:
        return ConfigService.C_LOCAL_WAV_TX_SR

    @staticmethod
    def get_local_wav_tx_duration() -> float:
        return ConfigService.C_LOCAL_WAV_TX_DURATION

    @dataclass_json
    @dataclass
    class Config:
        tx_locator: str
        tx_latitude: float
        tx_longitude: float
        ant_rotator_service: str
        ant_rotator_device: str
        radio_control_service: str
        radio_control_device: str
        user_login_password: str
        hostname: str
        port: int
        enable_auth: bool
        enable_https: bool

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
        assert self._config.tx_locator is not None
        assert self._config.tx_latitude is not None
        assert self._config.tx_longitude is not None
        self._startup_time: str = TimeUtil.get_current_time_utc_str()

        # Set wav file properties
        assert os.path.exists(ConfigService.C_LOCAL_WAV_TX_FILE)
        y, sr = librosa.load(ConfigService.C_LOCAL_WAV_TX_FILE)
        ConfigService.C_LOCAL_WAV_TX_SR = sr
        ConfigService.C_LOCAL_WAV_TX_DURATION = round(librosa.get_duration(y=y, sr=sr), 3)
        assert ConfigService.C_LOCAL_WAV_TX_SR > 0
        assert ConfigService.C_LOCAL_WAV_TX_DURATION > 0
        del y, sr

        print("- ConfigService initialized.")

    def get_config(self) -> Config:
        return self._config

    def get_startup_time(self) -> str:
        return self._startup_time

# if __name__ == '__main__':
#     # sample_config = ConfigService.Config(tx_locator='JN59')
#     # ConfigService.to_json_file(sample_config, ConfigService.C_LOCAL_FILE)
