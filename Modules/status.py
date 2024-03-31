class Status:
    def __init__(self, name: str, severity: int, is_sick: bool):
        self.name = name
        self.severity = severity
        self.is_sick = is_sick

    def effect(self):
        pass
