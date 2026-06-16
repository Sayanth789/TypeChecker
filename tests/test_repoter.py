from diagnostics.reporter import DiagnosticReporter

# Initital state
def test_reporter_initial_state():
    r = DiagnosticReporter()
    assert r.errors == []

# Single error 
def test_single_error():
    r = DiagnosticReporter()

    r.error("Something went wrong")

    assert r.errors == ["Something went wrong"]

# Multiple errors 
def test_multiple_errors():
    r = DiagnosticReporter()

    r.error("error 1") 
    r.error("error 2")

    assert r.errors == ["error 1", "error 2"]   