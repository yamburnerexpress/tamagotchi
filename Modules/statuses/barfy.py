from Modules.status import Status

class Barfy(Status):
    def __init__(self):
        super().__init__(
            name="barfy",
            severity=1
        )
