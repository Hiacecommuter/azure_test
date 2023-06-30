from flask import Flask, render_template, flash, redirect, url_for
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/countdown/')
def countdown():
    olympics = datetime(2032, 7, 23, 10, 0, 0).timestamp()
    now = datetime.now().timestamp()
    diff_sec = round(olympics - now)
    return render_template("countdown.html", total_sec=diff_sec)

@app.route('/sudoku/')
def sudoku():
    return render_template("sudoku.html")

@app.route("/stopwatch/")
def stopwatch():
    return render_template("stopwatch.html")

@app.errorhandler(404)
def page_not_found(e):
    flash("Something goes wrong ... \n That page cannot be found")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.secret_key = "This is a long sec key"
    app.run(debug=True)
