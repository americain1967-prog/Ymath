from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/cours')
def cours():
    return render_template("cours.html")

@app.route('/exercices')
def exercices():
    return render_template("exercices.html")

@app.route('/quiz')
def quiz():
    return render_template("quiz.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
