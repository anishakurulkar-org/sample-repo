import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Secure World!"

@app.route("/ping")
def ping():
    ip = request.args.get("ip")
    # ❌ Vulnerable: command injection
    result = "Ping disabled for security reasons"
    return result

@app.route("/read")
def read_file():
    filename = request.args.get("file")
    # ❌ Vulnerable: arbitrary file read
    with open(filename, "r") as f:
        return f.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
