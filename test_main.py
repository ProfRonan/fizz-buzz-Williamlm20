import builtins
import importlib
import io
import sys

import pytest
from pytest import MonkeyPatch


@pytest.mark.parametrize(
    "test_input",
    [
        ("3", "Fizz"),
        ("6", "Fizz"),
        ("9", "Fizz"),
    ],
)
def test_fizz(monkeypatch: MonkeyPatch, test_input: str):
    mocked_input = lambda prompt="": test_input
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    assert "Fizz" in mocked_stdout.getvalue().strip()
    assert "Buzz" not in mocked_stdout.getvalue().strip()
    assert "FizzBuzz" not in mocked_stdout.getvalue().strip()
    assert test_input not in mocked_stdout.getvalue().strip()


@pytest.mark.parametrize(
    "test_input",
    [
        ("5", "Buzz"),
        ("10", "Buzz"),
        ("20", "Buzz"),
    ],
)
def test_buzz(monkeypatch: MonkeyPatch, test_input: str):
    mocked_input = lambda prompt="": test_input
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    assert "Fizz" not in mocked_stdout.getvalue().strip()
    assert "Buzz" in mocked_stdout.getvalue().strip()
    assert "FizzBuzz" not in mocked_stdout.getvalue().strip()
    assert test_input not in mocked_stdout.getvalue().strip()


@pytest.mark.parametrize(
    "test_input",
    [
        ("0", "FizzBuzz"),
        ("15", "FizzBuzz"),
        ("30", "FizzBuzz"),
    ],
)
def test_fizz_buzz(monkeypatch: MonkeyPatch, test_input: str):
    mocked_input = lambda prompt="": test_input
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    assert "FizzBuzz" in mocked_stdout.getvalue().strip()
    assert test_input not in mocked_stdout.getvalue().strip()


@pytest.mark.parametrize(
    "test_input",
    [
        ("1", "1"),
        ("2", "2"),
        ("4", "4"),
    ],
)
def test_none(monkeypatch: MonkeyPatch, test_input: str):
    mocked_input = lambda prompt="": test_input
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    assert "Fizz" not in mocked_stdout.getvalue().strip()
    assert "Buzz" not in mocked_stdout.getvalue().strip()
    assert "FizzBuzz" not in mocked_stdout.getvalue().strip()
    assert test_input in mocked_stdout.getvalue().strip()
