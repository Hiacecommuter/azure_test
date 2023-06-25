from flask import Flask
from datetime import date


app = Flask(__name__)

@app.route('/')
def home():
    Oly_date = date.fromisoformat("2032-07-23")
    today = date.today()
    return "<div><p>f"Countdown to Brisbane Olympic 2032: {Oly_date - today}"</p></div>"


if __name__ == "__main__":
    app.run()
