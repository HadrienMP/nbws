import re
import requests
from bs4 import BeautifulSoup


def get_next_stop_times(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    table_cells = soup.find(id="prochains_passages").select("tr td")

    times = list()
    for i in range(0, len(table_cells), 2):
        times.append((table_cells[i].string, __to_int(table_cells[i+1].string)))

    return times


def __to_int(raw_time):
    if raw_time and re.match("\d+\smn", raw_time):
        return int(raw_time.split(" ")[0])
    else:
        return 0
