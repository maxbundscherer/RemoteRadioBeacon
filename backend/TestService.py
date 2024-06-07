from dataclasses import dataclass


class TestService:
    @dataclass
    class TestItem:
        name: str
        description: str

    @staticmethod
    def get_test_items() -> [TestItem]:
        return [
            TestService.TestItem(
                name='Test 1',
                description='This is a test item.'
            ),
            TestService.TestItem(
                name='Test 2',
                description='This is another test item.'
            )
        ]
