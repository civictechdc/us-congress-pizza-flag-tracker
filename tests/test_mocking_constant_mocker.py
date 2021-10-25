from pytest_mock import mocker

import mock_examples.functions
from mock_examples.functions import double

class Test:
    def abc(self):
        mocker.patch.object()

# note that I'm mocking the module when it is imported, not where CONSTANT_A is from
def test_mocking_constant_a(mocker):
    mocker.patch.object(mock_examples.functions, 'CONSTANT_A', 2)
    expected = 4
    actual = double()


    assert expected == actual


def test_mocking_constant_twice_in_same_test(mocker):
    mocker.patch.object(mock_examples.functions, 'CONSTANT_A', 3)
    expected_1 = 6
    actual_1 = double()

    mocker.patch.object(mock_examples.functions, 'CONSTANT_A', 10)
    expected_2 = 20
    actual_2 = double()

    assert expected_1 == actual_1
    assert expected_2 == actual_2
