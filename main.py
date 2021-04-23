from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/portfolio")
def portfolio():
    return render_template("/portfolio.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("fakebook.html")


@app.route("/portfolio/boogle")
def boogle():
    return render_template("boogle.html")


@app.route("/portfolio/hair-salon")
def hair_salon():
    return render_template("hair-salon.html")


if __name__ == "__main__":
    app.run(use_reloader=True, port=8080)
