from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        'title': 'Frostspire',
        'date': 'June 14, 2025',
        'type': 'Web App',
        'description': 'A blog platform inspired by cinematic designs, built with PHP and MySQL.',
        'image': 'project_bg.jpg',
        'link': 'https://github.com/yourgithub/frostspire'
    },
    # Add more projects here
]

@app.route("/")
def home():
    return render_template("index.html", project=projects[0], projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
