from collections import OrderedDict

from flask import Flask, abort, jsonify
from flask.templating import render_template

from ratp_client import get_next_stop_times

app = Flask(__name__)
LINES = {
    "Maison -> Darty": "http://www.ratp.fr/horaires/fr/ratp/bus/prochains_passages/PP/B102/102_15_42/R",
    "Darty -> Maison": "http://www.ratp.fr/horaires/fr/ratp/bus/prochains_passages/PP/B102/102_6_53/A"
}


@app.route('/')
def index():
    lines = OrderedDict()
    lines["Maison -> Darty"] = to_display(get_next_stop_times(LINES["Maison -> Darty"]))
    lines["Darty -> Maison"] = to_display(get_next_stop_times(LINES["Darty -> Maison"]))

    return render_template("index.html", lines=lines)


@app.route("/line/<key>")
def line(key):
    if key in LINES.keys():
        return jsonify(to_display(get_next_stop_times(LINES.get(key))))
    else:
        abort(404)


def to_display(times):
    return [(to_display_destination(time), time[1], time[2].strftime('%Hh%M')) for time in times]


def to_display_destination(time):
    return str(time[0]).replace("-", " ")


if __name__ == '__main__':
    app.run(debug=True)
