from flask import Flask, render_template, request, redirect, jsonify, send_file
import pandas as pd
import io
import json

app = Flask(__name__)

tasks = []


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():

    task = {
        "id": len(tasks)+1,
        "title": request.form["title"],
        "description": request.form["description"],
        "status": request.form["status"]
    }

    tasks.append(task)

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):

    global tasks

    tasks = [t for t in tasks if t["id"] != id]

    return redirect("/")


@app.route("/edit/<int:id>")
def edit(id):

    task = next((x for x in tasks if x["id"] == id), None)

    return render_template("edit.html", task=task)


@app.route("/update/<int:id>", methods=["POST"])
def update(id):

    for task in tasks:

        if task["id"] == id:

            task["title"] = request.form["title"]
            task["description"] = request.form["description"]
            task["status"] = request.form["status"]

    return redirect("/")


@app.route("/import", methods=["POST"])
def import_excel():

    file = request.files["excel"]

    df = pd.read_excel(file)

    for _, row in df.iterrows():

        tasks.append({

            "id": len(tasks)+1,
            "title": row["Title"],
            "description": row["Description"],
            "status": row["Status"]

        })

    return redirect("/")


@app.route("/download")
def download():

    data = json.dumps(tasks, indent=4)

    file = io.BytesIO()

    file.write(data.encode())

    file.seek(0)

    return send_file(
        file,
        download_name="tasks.json",
        as_attachment=True,
        mimetype="application/json"
    )


if __name__ == "__main__":
    app.run(debug=True)