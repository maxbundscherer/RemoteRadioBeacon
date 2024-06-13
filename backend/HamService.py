from dataclasses import dataclass

from dataclasses_json import dataclass_json

from backend.ConfigService import ConfigService
from backend.antRotator.AbstractAntRotatorService import AbstractAntRotatorService, AntRotatorState
from backend.antRotator.DummyAntRotatorService import DummyAntRotatorService
from backend.radioControl.AbstractRadioControlService import AbstractRadioControlService, RadioState
from backend.radioControl.DummyRadioControlService import DummyRadioControlService
from backend.utils.LocationUtil import LocationUtil


class HamService:
    @dataclass_json
    @dataclass
    class AntRotorParams:
        maidenhead: str
        latitude: float
        longitude: float
        distance: float
        azimuth: float

    def __init__(self, config_service: ConfigService):

        if config_service.get_config().ant_rotator_service == 'DummyService':
            self._ant_rotator_service: AbstractAntRotatorService = DummyAntRotatorService(config_service)
        else:
            raise Exception("Unknown AntRotatorService", config_service.get_config().ant_rotator_service)

        if config_service.get_config().radio_control_service == 'DummyService':
            self._radio_control_service: AbstractRadioControlService = DummyRadioControlService(config_service)
        else:
            raise Exception("Unknown RadioControlService", config_service.get_config().radio_control_service)

        self._config_service: ConfigService = config_service

        print("- HamService initialized.")

    def get_ant_rotator_state(self) -> AntRotatorState:
        return self._ant_rotator_service.get_state()

    def set_ant_rotator_azimuth(self, azimuth: float):
        self._ant_rotator_service.set_azimuth(azimuth)

    def set_ant_rotator_elevation(self, elevation: float):
        self._ant_rotator_service.set_elevation(elevation)

    def get_radio_state(self) -> RadioState:
        return self._radio_control_service.get_state()

    def set_radio_frequency(self, frequency: int):
        self._radio_control_service.set_frequency(frequency)

    def set_radio_power(self, power: int):
        self._radio_control_service.set_power(power)

    def set_radio_mode(self, mode: str):
        self._radio_control_service.set_mode(mode)

    def start_radio_tx(self):
        self._radio_control_service.start_transmit()

    def stop_radio_tx(self):
        self._radio_control_service.stop_transmit()

    def calc_ant_rotor_params_by_gps(self, latitude: float, longitude: float) -> AntRotorParams:

        gps_0: LocationUtil.Coordinate = LocationUtil.Coordinate(latitude=self._config_service.get_config().tx_latitude,
                                                                 longitude=self._config_service.get_config().tx_longitude)

        gps_1: LocationUtil.Coordinate = LocationUtil.Coordinate(latitude=latitude, longitude=longitude)

        da: LocationUtil.DistanceAzimuth = LocationUtil.calc_distance_azimuth(gps_0, gps_1)

        return HamService.AntRotorParams(
            maidenhead=LocationUtil.coordinates_to_maidenhead(gps_1),
            latitude=gps_1.latitude,
            longitude=gps_1.longitude,
            distance=round(da.distance, 3),
            azimuth=round(da.azimuth, 2)
        )

    def calc_ant_rotor_params_by_mai(self, maidenhead: str) -> AntRotorParams:

        gps_0: LocationUtil.Coordinate = LocationUtil.Coordinate(latitude=self._config_service.get_config().tx_latitude,
                                                                 longitude=self._config_service.get_config().tx_longitude)

        gps_1: LocationUtil.Coordinate = LocationUtil.maidenhead_to_coordinates(maidenhead)

        da: LocationUtil.DistanceAzimuth = LocationUtil.calc_distance_azimuth(gps_0, gps_1)

        return HamService.AntRotorParams(
            maidenhead=maidenhead,
            latitude=gps_1.latitude,
            longitude=gps_1.longitude,
            distance=round(da.distance, 3),
            azimuth=round(da.azimuth, 2)
        )
