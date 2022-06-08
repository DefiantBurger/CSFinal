import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello! this is the main page <h1>HELLO</h1><br><a href=\"output\">output</a>"


@app.route("/output/")
def output():
    return "<br>".join(f"<a href=\"{path}\">{path}</a>" for path in os.listdir('../output'))


@app.route("/output/<project>/<file>")
def outputFile(project, file):
    file += ".java"
    with open(f'../output/{project}/{file}', 'r') as f:
        return "<br>".join(f.read().split("\n"))


@app.route("/output/<project>/")
def outputFolder(project):
    return "<br>".join(
        f"<a href=\"{path.removesuffix('.java')}\">{path}</a>" for path in os.listdir(f'../output/{project}'))


if __name__ == "__main__":
    app.run(debug=True)