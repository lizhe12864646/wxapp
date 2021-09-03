import pytest
from mock_method import *

def test_get_url(mocker):
    mocker.patch('mock_method.send_request',return_value=300)
    assert invoke_method('https://www.python.org') == 300


if __name__ == '__main__':
    pytest.main()