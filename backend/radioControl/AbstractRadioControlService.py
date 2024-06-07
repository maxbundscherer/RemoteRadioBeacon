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
        print("- RadioControlService initialized.")

    def test(self):
        raise NotImplementedError("Method must be implemented in derived classes.")

    def get_state(self) -> RadioState:
        raise NotImplementedError("Method must be implemented in derived classes.")
