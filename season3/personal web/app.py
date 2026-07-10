from flask import Flask, render_template

app = Flask(__name__)

profile = {
    "name": "Qazal Abdi",
    "about": "Full Stack Developer | WordPress Developer | Python Enthusiast"
}

skills = [
    "Python",
    "Flask",
    "HTML5",
    "CSS3",
    "JavaScript",
    "React",
    "WordPress",
    "Docker",
    "Git"
]

projects = [
    {
        "title": "Personal Portfolio",
        "description": "A responsive portfolio website built with Flask.",
    },
    {
        "title": "Task Manager",
        "description": "Simple task management application using Flask.",
    },
    {
        "title": "Blog Website",
        "description": "Personal blog developed using Flask and SQLite.",
    }
]


@app.route("/")
def home():
    return render_template("home.html", profile=profile)


@app.route("/skills")
def skill_page():
    return render_template("skills.html",
                           profile=profile,
                           skills=skills)


@app.route("/projects")
def project_page():
    return render_template("projects.html",
                           profile=profile,
                           projects=projects)


if __name__ == "__main__":
    app.run(debug=True)