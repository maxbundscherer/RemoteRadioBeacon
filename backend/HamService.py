from backend.ham.AntennaRotatorService import AntennaRotatorService
from backend.ham.RadioControlService import RadioControlService


class HamService:

    def __init__(self):
        self._antenna_rotator_service = AntennaRotatorService()
        self._radio_control_service = RadioControlService()
        print("- HamService initialized.")
