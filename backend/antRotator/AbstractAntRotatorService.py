from dataclasses import dataclass


@dataclass
class AntRotatorState:
    azimuth: float
    elevation: float


class AbstractAntRotatorService:

    def __init__(self):
        self._state: AntRotatorState = AntRotatorState(
            azimuth=-1,
            elevation=-1
        )
        print("- AntRotatorService initialized.")

    def startup_test(self):
        raise NotImplementedError("Method must be implemented in derived classes.")

    def get_state(self) -> AntRotatorState:
        raise NotImplementedError("Method must be implemented in derived classes.")
