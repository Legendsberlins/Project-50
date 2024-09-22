from flask import Flask, render_template, request

app = Flask(__name__) #convention in flask to create a web application in python is that you create a variable called app and assign it the return value of Flask function.

REGISTRANTS = {}

TEAMS = ["Brooklyn Nets", "Los Angeles Lakers", "Golden State Warriors"]

@app.route("/") #any order of methods
def form():
    return render_template("index.html", teams = TEAMS) #teams is a placeholder for the list SPORTS

@app.route("/success", methods = ["POST"])
def success():
    name = request.form.get("name")
    if not name:
        return render_template("failure.html")

    team = request.form.get("team")
    if team not in TEAMS:
        return render_template("failure.html")

    REGISTRANTS[name] = team
    return render_template("success.html")

@app.route("/registrants")
def database():
    return render_template("registrants.html", placeholder = REGISTRANTS)