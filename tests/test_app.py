# tests/test_app.py
import pytest
from src.app import add, divide

# # 1. Successful Test Case
# def test_add_success():
#     assert add(2, 3) == 5

# # 2. Successful Test Case (Exception handling)
# def test_divide_by_zero_success():
#     with pytest.raises(ValueError):
#         divide(10, 0)

# 3. Intentionally Failed Test Case (For demonstration)
def test_add_failure():
    assert add(2, 2) == 5  # This will fail because 2 + 2 = 4
