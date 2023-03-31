import builtins
import importlib
import io
import sys

import pytest
from pytest import MonkeyPatch


@pytest.mark.parametrize(
    "test_input",
    [
        ("3"),
        ("6"),
        ("9"),
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
        ("5"),
        ("10"),
        ("20"),
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
        ("0"),
        ("15"),
        ("30"),
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
        ("1"),
        ("2"),
        ("4"),
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
