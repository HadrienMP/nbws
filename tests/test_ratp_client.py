from unittest.mock import patch

from assertpy.assertpy import assert_that

from ratp_client import get_next_stop_times
from tests.utils import mock_request_get, mock_service_over


def test_get_next_102_to_gambetta_in_integration():
    times = get_next_stop_times("http://www.ratp.fr/horaires/fr/ratp/bus/prochains_passages/PP/B102/102_15_42/R") \
            + get_next_stop_times("http://www.ratp.fr/horaires/fr/ratp/bus/prochains_passages/PP/B102/102_6_53/A")

    assert_that(len(times)).is_greater_than_or_equal_to(4)
    assert_that(times[0][0]).matches(r'[\w\s]+')
    assert_that(times[0][1]).is_greater_than_or_equal_to(0)


@patch("requests.get")
def test_get_next_102_to_gambetta(requests_mock):
    mock_request_get(requests_mock, ("Gambetta", 15), ("Mairie de Montreuil", 18))

    times = get_next_stop_times("an url")

    assert_that(times).contains(("Gambetta", 15), ("Mairie de Montreuil", 18))


@patch("requests.get")
def test_service_over(requests_mock):
    mock_service_over(requests_mock)

    times = get_next_stop_times("an url")

    assert_that(times).contains(("SERVICE", 0), ("NON COMMENCE", 0))
