import os
from flask import Flask, render_template, request
from sqla_wrapper import SQLAlchemy
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

db_url = os.getenv("DATABASE_URL", "sqlite:///db.sqlite").replace("postgres://", "postgresql://", 1)
db = SQLAlchemy(db_url)


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String, unique=False)
    client_email = db.Column(db.String, unique=False)
    client_subject = db.Column(db.String, unique=False)
    client_message = db.Column(db.String, unique=False)


app = Flask(__name__)
db.create_all()


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")

    elif request.method == "POST":
        client_name = request.form.get("name")
        client_email = request.form.get("email")
        client_subject = request.form.get("subject")
        client_message = request.form.get("message")

        body = """
            name: {0}, 
            sender_email: {1},
            message: {2}.
        """.format(client_name, client_email, client_message)

        email = Mail(from_email="blazyy@gmail.com",
                     to_emails="blazyy@gmail.com",
                     subject=client_subject,
                     html_content=body)
        email.reply_to = client_email

        # DELETE API KEY BEFORE UPLOADING TO GITHUB!!!!!!!
        sg_key = os.environ.get("SENDGRID_API_KEY")

        sg = SendGridAPIClient(sg_key)
        response = sg.send(email)

        return render_template("message.html")
    else:
        return render_template("error.html")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/portfolio")
def portfolio():
    return render_template("/portfolio.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/services")
def services():
    return render_template("services.html")


# attachments
@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("fakebook.html")


@app.route("/portfolio/boogle")
def boogle():
    return render_template("boogle.html")


@app.route("/portfolio/hair-salon")
def hair_salon():
    return render_template("hair-salon.html")


@app.route("/portfolio/hans")
def anz_hans():
    return render_template("anz-index.html")


if __name__ == "__main__":
    app.run(use_reloader=True)
