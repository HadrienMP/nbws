from collections import OrderedDict

from flask import Flask
from flask.templating import render_template

from ratp_client import get_next_stop_times

app = Flask(__name__)


@app.route('/')
def index():
    lines = OrderedDict()
    lines["Maison -> Darty"] = get_next_stop_times("http://www.ratp.fr/horaires/fr/ratp/bus/prochains_passages/PP/B102/102_15_42/R")
    lines["Darty -> Maison"] = get_next_stop_times("http://www.ratp.fr/horaires/fr/ratp/bus/prochains_passages/PP/B102/102_6_53/A")

    return render_template("index.html", lines=lines)


if __name__ == '__main__':
    app.run(debug=True)
