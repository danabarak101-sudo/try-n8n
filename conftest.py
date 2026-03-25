def pytest_addoption(parser):
    parser.addoption("--machine_name", action="store")
    parser.addoption("--version", action="store")
    parser.addoption("--user", action="store")
    parser.addoption("--password", action="store")
