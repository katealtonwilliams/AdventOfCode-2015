import pytest
from unittest.mock import mock_open, patch
from typing import Callable, Generator


@pytest.fixture
def mock_file_with_multiple_lines() -> Generator[Callable]:
    with patch("builtins.open", mock_open()) as mock_raw_data:

        def _set_mock_data(input_data: str = "data"):
            mock_raw_data.return_value.readlines.return_value = input_data

        yield _set_mock_data
