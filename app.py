from flask import Flask, render_template, request, redirect, url_for
from models import User
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config.from_object("config.Config")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Verifying login credentials.
        return redirect(url_for("dashboard"))
    return render_template("login.html", form=form)


@app.route("/register", method=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Creating a new user.
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/dashboard")
def dashboard():
    # Displaying dashboard
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
