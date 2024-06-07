import json
import os
from dataclasses import dataclass
from dataclasses_json import dataclass_json


class ConfigService:
    C_LOCAL_FILE = 'config.json'

    @dataclass_json
    @dataclass
    class Config:
        local_locator: str

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
        print("- ConfigService initialized.")

    def get_config(self) -> Config:
        return self._config

# if __name__ == '__main__':
#     # sample_config = ConfigService.Config(local_locator='JN59')
#     # ConfigService.to_json_file(sample_config, ConfigService.C_LOCAL_FILE)