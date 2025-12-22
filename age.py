from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def age_calculator():
    age = None
    if request.method == "POST":
        year = int(request.form["year"])
        month = int(request.form["month"])
        day = int(request.form["day"])

        today = date.today()
        age = today.year - year
        if (today.month, today.day) < (month, day):
            age -= 1

    return render_template("index.html", age=age)


if __name__ == "__main__":
    app.run(debug=True)
[[-2, 1, 3, 5]]
[]
