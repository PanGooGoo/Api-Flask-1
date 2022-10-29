from crypt import methods
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        day = request.form["day"]
        mood = request.form["mood"]
        if mood == "Pissed":
            pred = "This is NOT going to be a nice day!!!! Good luck!"
        if mood == "Not Pissed":
            pred = "ILY"
        return render_template("index.html", pred=str(pred))

    return render_template("index.html")


# if __name__ == "__main__":
#    app.run()
