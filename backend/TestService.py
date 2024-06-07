import time
from dataclasses import dataclass


class TestService:
    @dataclass
    class TestItem:
        name: str
        description: str
        test_int: int = 0
        created_at: str = ''

    def __init__(self):
        self._test_description = 'This is a test item.'
        self._test_int: int = 42

    def set_test_description(self, description: str):
        self._test_description = description

    def set_test_int(self, test_int: int):
        self._test_int = test_int

    def get_test_item(self) -> TestItem:
        return TestService.TestItem(
            name='Test 1',
            description=self._test_description,
            test_int=self._test_int,
            created_at=time.strftime('%Y-%m-%d %H:%M:%S')
        )
