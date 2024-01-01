from pyka import lib
import pytest

class TestExample:
    def test_decorate(self, mocker):
        mocked_func = mocker.patch('pyka.lib.decorate')
        mocked_func.return_value = 'fish'
        assert lib.decorate("AAA") == 'fish'
        mocked_func.assert_called_once_with("AAA")
    def test_exception(self, mocker):
        with pytest.raises(ZeroDivisionError):
            1 / 0
