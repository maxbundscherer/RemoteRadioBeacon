from backend.antRotator.AbstractAntRotatorService import AbstractAntRotatorService, AntRotatorState


class DummyAntRotatorService(AbstractAntRotatorService):

    def test(self):
        pass

    def get_state(self) -> AntRotatorState:
        return self._state
