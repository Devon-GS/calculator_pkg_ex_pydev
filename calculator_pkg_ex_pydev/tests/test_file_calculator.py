from calculator_pkg_ex_pydev import FileCalculator


def test_file_calculator() -> None:
    assert FileCalculator().add_file() == 6, "Add File Failed"