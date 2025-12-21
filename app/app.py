from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "../logs/auth.log"

HTML = """
<h2>Secure Login</h2>
<form method="POST">
  Username: <input name="username"><br><br>
  Password: <input name="password" type="password"><br><br>
  <button type="submit">Login</button>
</form>
<p>{{ msg }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        ip = request.remote_addr
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Fake authentication
        if username == "admin" and password == "password123":
            msg = "Login Successful"
            status = "SUCCESS"
        else:
            msg = "Invalid Credentials"
            status = "FAILED"

        with open(LOG_FILE, "a") as f:
            f.write(f"{time} | {ip} | {username} | {status}\n")

    return render_template_string(HTML, msg=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
