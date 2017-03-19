from unittest.mock import patch

from assertpy.assertpy import assert_that

from ratp_client import get_next_stop_times
from tests.utils import mock_request_get, mock_service_over


def next_102s():
    return get_next_stop_times()


def test_get_next_102_to_gambetta_in_integration():
    times = next_102s()

    assert_that(len(times)).is_greater_than_or_equal_to(2)
    assert_that(times[0][0]).matches(r'[\w\s]+')
    assert_that(times[0][1]).is_greater_than_or_equal_to(0)


@patch("requests.get")
def test_get_next_102_to_gambetta(requests_mock):
    mock_request_get(requests_mock, ("Gambetta", 15), ("Mairie de Montreuil", 18))

    times = next_102s()

    assert_that(times).contains(("Gambetta", 15), ("Mairie de Montreuil", 18))


@patch("requests.get")
def test_service_over(requests_mock):
    mock_service_over(requests_mock)

    times = next_102s()

    assert_that(times).contains_only(("SERVICE", 0), ("NON COMMENCE", 0))
