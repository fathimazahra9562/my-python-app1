
import os
import subprocess
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Hardcoded Secret
API_SECRET_KEY = os.getenv("API_SECRET_KEY", "")
@app.route("/user")
def get_user():
    username = request.args.get("username")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SQL Injection Risk
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return "User query processed"

@app.route("/run")
def run_command():
    cmd = request.args.get("cmd")

    # Command Injection Risk
    os.system(cmd)
    subprocess.call(cmd, shell=True)

    return "Command executed"

if __name__ == "__main__":
    app.run(debug=True)
