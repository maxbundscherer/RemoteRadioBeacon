from dataclasses import dataclass


class AbstractAntRotatorService:
    @dataclass
    class AntRotatorState:
        azimuth: float
        elevation: float

    def __init__(self):
        self._state: AbstractAntRotatorService.AntRotatorState = AbstractAntRotatorService.AntRotatorState(
            azimuth=-1,
            elevation=-1
        )
        print("- AntRotatorService initialized.")

    def test(self):
        raise NotImplementedError("Method must be implemented in derived classes.")

    def get_state(self) -> AntRotatorState:
        raise NotImplementedError("Method must be implemented in derived classes.")
