from collections import OrderedDict

from flask import Flask, abort
from flask.templating import render_template

from ratp_client import get_next_stop_times

app = Flask(__name__)
lines = {
    "Maison -> Darty": "http://www.ratp.fr/horaires/fr/ratp/bus/prochains_passages/PP/B102/102_15_42/R",
    "Darty -> Maison": "http://www.ratp.fr/horaires/fr/ratp/bus/prochains_passages/PP/B102/102_6_53/A"
}


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/line/<key>")
def line(key):
    if key in lines.keys():
        return render_template("line.html", stop=key, times=get_next_stop_times(lines.get(key)))
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
