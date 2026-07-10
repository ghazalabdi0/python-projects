from flask import Flask, render_template, request, redirect

app = Flask(__name__)

records = []

@app.route("/")
def index():
    return render_template("index.html", records=records)


@app.route("/add", methods=["POST"])
def add():

    name = request.form.get("name", "").strip()
    age = request.form.get("age", "").strip()
    interest = request.form.get("interest", "")
    level = request.form.get("level", "")
    description = request.form.get("description", "")

    # اعتبارسنجی نام
    if not name:
        return "Name cannot be empty."

    # اعتبارسنجی سن
    try:
        age = int(age)
    except ValueError:
        return "Age must be a number."

    records.append({
        "name": name,
        "age": age,
        "interest": interest,
        "level": level,
        "description": description
    })

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)