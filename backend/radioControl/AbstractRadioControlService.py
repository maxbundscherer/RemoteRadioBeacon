from dataclasses import dataclass


@dataclass
class RadioState:
    frequency: float
    mode: str
    is_transmitting: bool


class AbstractRadioControlService:

    def __init__(self):
        self._state: RadioState = RadioState(
            frequency=-1,
            mode='N/A',
            is_transmitting=False
        )
        assert self._startup_test()
        print("- RadioControlService initialized.")

    def get_state(self) -> RadioState:
        self._trigger_update_state()
        return self._state

    @staticmethod
    def _startup_test() -> bool:
        raise NotImplementedError("Method must be implemented in derived classes.")

    def _trigger_update_state(self):
        raise NotImplementedError("Method must be implemented in derived classes.")
