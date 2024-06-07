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
        assert self._startup_test()
        print("- AntRotatorService initialized.")

    def get_state(self) -> AntRotatorState:
        self._trigger_update_state()
        return self._state

    @staticmethod
    def _startup_test() -> bool:
        raise NotImplementedError("Method must be implemented in derived classes.")

    def _trigger_update_state(self):
        raise NotImplementedError("Method must be implemented in derived classes.")
