from flask import Flask
import socket, os

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello, je suis Prenom Nom — pod {socket.gethostname()}"

@app.route("/healthz")
def health():
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
