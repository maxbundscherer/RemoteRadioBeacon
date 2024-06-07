from dataclasses import dataclass


class AbstractRadioControlService:
    @dataclass
    class RadioState:
        frequency: float
        mode: str
        is_transmitting: bool

    def __init__(self):
        self._state: AbstractRadioControlService.RadioState = AbstractRadioControlService.RadioState(
            frequency=-1,
            mode='N/A',
            is_transmitting=False
        )
        print("- RadioControlService initialized.")

    def test(self):
        raise NotImplementedError("Method must be implemented in derived classes.")

    def get_state(self) -> RadioState:
        raise NotImplementedError("Method must be implemented in derived classes.")
