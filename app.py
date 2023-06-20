from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return "<div><p>welcome to the test home</p></div>"


if __name__ == "__main__":
    app.run()