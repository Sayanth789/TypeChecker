class DiagnosticReporter:
    def __init__(self):
        self.errors = []

    def error(self, message):
        self.errors.append(message)