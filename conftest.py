def pytest_addoption(parser):
    parser.addoption("--mname", action="store", help="machine name")
    parser.addoption("--mver", action="store", help="version")
    parser.addoption("--muser", action="store", help="user")
    parser.addoption("--mpass", action="store", help="password")
