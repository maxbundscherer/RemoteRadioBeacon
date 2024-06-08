from dataclasses import dataclass
import maidenhead as mh


class LocationUtil:
    @dataclass
    class Coordinate:
        latitude: float
        longitude: float

    @staticmethod
    def maidenhead_to_coordinates(loc: str) -> Coordinate:
        c = mh.to_location(loc)

        return LocationUtil.Coordinate(
            latitude=c[0],
            longitude=c[1]
        )


if __name__ == '__main__':
    gps_0: LocationUtil.Coordinate = LocationUtil.maidenhead_to_coordinates("JN59NK18")
    gps_1: LocationUtil.Coordinate = LocationUtil.maidenhead_to_coordinates("JN58MP36")

    print(gps_0)
    print(gps_1)
