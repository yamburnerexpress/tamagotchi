from Modules.status import Status

class Healthy(Status):
    def __init__(self):
        super().__init__(
            name="healthy",
            severity=0
        )
