from backend.ham.AntRotatorService import AntRotatorService
from backend.ham.RadioControlService import RadioControlService


class HamService:

    def __init__(self):
        self._ant_rotator_service: AntRotatorService = AntRotatorService()
        self._radio_control_service: RadioControlService = RadioControlService()
        print("- HamService initialized.")
