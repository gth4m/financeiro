from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, E AQUI SERVIREMOS TODO ESSE GLAMOUR!</p>"