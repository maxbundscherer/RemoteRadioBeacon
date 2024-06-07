class AbstractRadioControlService:

    def __init__(self):
        print("- RadioControlService initialized.")

    def test(self):
        raise NotImplementedError("Method must be implemented in derived classes.")
