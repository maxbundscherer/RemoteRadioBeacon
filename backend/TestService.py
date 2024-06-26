from dataclasses import dataclass

from backend.utils.TimeUtil import TimeUtil


class TestService:
    @dataclass
    class TestItem:
        name: str
        description: str
        test_int: int = 0
        created_at: str = ''

    def __init__(self):
        self._test_description = 'TestDesc'
        self._test_int: int = 42

    def set_test_description(self, description: str):
        self._test_description = description

    def get_test_description(self) -> str:
        return self._test_description

    def set_test_int(self, test_int: int):
        self._test_int = test_int

    def get_test_int(self) -> int:
        return self._test_int

    def get_test_item(self) -> TestItem:
        return TestService.TestItem(
            name='Test 1',
            description=self._test_description,
            test_int=self._test_int,
            created_at=TimeUtil.get_current_time_utc_str()
        )
