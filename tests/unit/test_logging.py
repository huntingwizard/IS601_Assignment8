import logging
import pytest
from app.operations import add, subtract, multiply, divide

def test_add_logs_result(caplog):
    with caplog.at_level(logging.INFO):
        add(2, 3)
    assert "add(2, 3) = 5" in caplog.text

def test_subtract_logs_result(caplog):
    with caplog.at_level(logging.INFO):
        subtract(5, 3)
    assert "subtract(5, 3) = 2" in caplog.text

def test_multiply_logs_result(caplog):
    with caplog.at_level(logging.INFO):
        multiply(2, 3)
    assert "multiply(2, 3) = 6" in caplog.text

def test_divide_logs_result(caplog):
    with caplog.at_level(logging.INFO):
        divide(6, 3)
    assert "divide(6, 3) = 2.0" in caplog.text

def test_divide_by_zero_logs_error(caplog):
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError):
            divide(1, 0)
    assert "division by zero" in caplog.text