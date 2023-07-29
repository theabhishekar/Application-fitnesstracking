from flask import Flask, render_template, request

app = Flask(__name__)

workout_entries = []

@app.route("/")
def index():
    return render_template("index.html", entries=workout_entries)

@app.route("/add", methods=["GET", "POST"])
def add_entry():
    if request.method == "POST":
        workout_name = request.form["workout_name"]
        duration = request.form["duration"]
        calories_burned = request.form["calories_burned"]
        workout_entries.append({"workout_name": workout_name, "duration": duration, "calories_burned": calories_burned})
    return render_template("add_entry.html")

if __name__ == "__main__":
    app.run(debug=True)
