from flask import Flask, render_template, Blueprint, session
from routes.login import login

app = Flask(__name__, static_folder="frontend", template_folder="frontend")
app.secret_key = "34343sffe2f2"


@app.route("/index")
def index():
    return render_template("templates/index.html")


app.register_blueprint(login)

if __name__ == "__main__":
    app.run(debug=True)