from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from cs50 import SQL

#configure flask
app = Flask(__name__)

#configure cookies session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#configure database
db = SQL("sqlite:///store.db")

@app.route("/")
def index():
   books = db.execute("SELECT * FROM books") #this is how we see all the books in index.html
   return render_template("books.html", books = books)

@app.route("/cart", methods = ["GET", "POST"])
def cart():

   #Ensures cart exists
   if "cart" not in session:
      session["cart"] = []

    #if cart isn't empty, append the id of the books into the cart list
    if request.method == "POST":
      id = request.form.get("id")
      if id:
         session["cart"].append(id)
      return redirect("/cart ")

     #request for books in shopping cart using 'GET'
     books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"])
     return render_template("cart.html", books = books)