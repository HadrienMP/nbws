from flask import Flask
from flask.templating import render_template

from ratp_client import get_next_stop_times

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", times=get_next_stop_times())


if __name__ == '__main__':
    app.run(debug=True)
