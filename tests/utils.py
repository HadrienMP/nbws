from os.path import dirname


def mock_service_over(requests_mock):
    with open(dirname(__file__) + "/resources/ratp_times_service_over.html") as f:
        requests_mock.return_value = ResponseMock(f.read())


def mock_request_get(requests_mock, first_stop, second_stop):

    with open(dirname(__file__) + "/resources/ratp_times.html") as f:
        page_format = f.read()

    page_content = page_format.format(first_stop[0], first_stop[1], second_stop[0], second_stop[1])
    requests_mock.return_value = ResponseMock(page_content)


class ResponseMock:
    def __init__(self, text):
        self.text = text