import re
from datetime import datetime, timedelta

import pytz
import requests
from bs4 import BeautifulSoup

utc = pytz.utc
paris = pytz.timezone("Europe/Paris")


def get_next_stop_times(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    table_cells = soup.find(id="prochains_passages").select("tr td")

    times = list()
    for i in range(0, len(table_cells), 2):
        destination = table_cells[i].string
        minutes_to_bus = __to_int(table_cells[i + 1].string)
        time = utc.localize(datetime.utcnow()).astimezone(paris) + timedelta(minutes=minutes_to_bus)
        times.append((destination, minutes_to_bus, time))

    return times


def __to_int(raw_time):
    if raw_time and re.match("\d+\smn", raw_time):
        return int(raw_time.split(" ")[0])
    else:
        return 0
