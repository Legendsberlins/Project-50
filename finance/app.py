import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Link user to account
    user_id = session["user_id"]
    transactions_db = db.execute(
        "SELECT Symbol, SUM(Shares) AS Shares, SUM(Price) AS Price FROM transactions WHERE User_id = ? GROUP BY Symbol", user_id)
    user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    # Extract the user cash from the dict
    user_cash = user_cash_db[0]["cash"]
    # Approx user_cash
    rounded_cash = round(user_cash, 2)

    return render_template("index.html", database=transactions_db, cashtml=rounded_cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # If GET , display form to buy stock
    if request.method == "POST":
        share = request.form.get("shares")
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Must provide symbol", 403)

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Invalid Stock")
        if not share:
            return apology("Must provide share")
        if not share.isdigit():
            return apology("Share must be a number")
        if int(share) < 0:
            return apology("Share must be positive")
        # Cost of a stock
        transaction_cost = int(share) * stock["price"]
        # Get id of user to see if they have enough balance
        user_id = session["user_id"]
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id) # :id and ? are the same
        user_cash = user_cash_db[0]["cash"] # Get user-cash as a real number not a list or dict

        # compare user_cash with transaction_cost
        if user_cash > transaction_cost:
            updated_cash = user_cash - transaction_cost
            db.execute("UPDATE users SET cash = ? WHERE id = ?", updated_cash, user_id)
            # Get date from datetime library
            date = datetime.datetime.now()
            # Insert transaction details into transaction table
            db.execute("INSERT INTO transactions (User_id, Symbol, Shares, Price, Date) VALUES (?,?,?,?,?)",
                       user_id, stock["symbol"], share, stock["price"], date)
            # Return success text using flash function
            flash("TRANSACTION SUCCESSFUL! STOCK BOUGHT")
            return redirect("/")

        return apology("Transaction Unsuccessful due to insufficient funds")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions_db = db.execute("SELECT * FROM transactions WHERE User_id = ?", user_id)
    return render_template("history.html", transactionshtml=transactions_db)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # When using POST, look up the stock symbol by calling the lookup function and display the results
    if request.method == "POST":
        symbol = request.form.get("symbol")
        stock = lookup(symbol)
        # If lookup is unsuccessful, return none i.e if the user typed in a stock that doesn't exist
        if stock == None:
            return apology("Invalid stock", 400)
        # If lookup is successful, function returns dictionary with name, price, symbol
        return render_template("quoted.html", name=stock["name"], price=stock["price"], symbol=stock["symbol"])
    # When requested via GET, display form to request stock quote
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # clear cookie session
    session.clear()

    # make sure user fills in all details
    if request.method == "POST":
        name = request.form.get('username')
        password = request.form.get('password')
        password_two = request.form.get('confirmation')
        if not name:
            return apology("must provide username", 400)
        elif not password:
            return apology("must provide password", 400)
        elif not password_two:
            return apology("Confirm password", 400)
        elif password != password_two:
            return apology("Passwords don't correspond", 400)

        # make sure username doesn't exist twice
        rows = db.execute("SELECT * FROM users WHERE username = ?", name)
        if len(rows) != 0:
            return apology("Username already exists")

        # Use generate_password_hash to generate a hash of the password instead of plain text
        password_generator = generate_password_hash(password)

        # Use SQL to include the user into the users table
        db.execute("INSERT INTO users (username, hash) VALUES (?,?)", name, password_generator)
        rows = db.execute("SELECT * FROM users WHERE username = ?", name)

        # log user in using session["user_id"] = id of the user who has been added
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        user_id = session["user_id"]
        user_symbols = db.execute(
            "SELECT Symbol FROM transactions WHERE User_id = ? GROUP BY Symbol HAVING SUM(Shares) > 0", user_id)

        return render_template("sell.html", symbols=[row["Symbol"] for row in user_symbols]) # to send rows of users symbols
    else:
        share = int(request.form.get("shares"))
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Must provide symbol", 403)

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Input stock")
        if not share:
            return apology("Must provide share")
        if share < 0:
            return apology("Share must be positive")

        # Cost of a stock
        transaction_cost = share * stock["price"]
        # Get id of user to see if they have enough balance
        user_id = session["user_id"]
        user_cash_db = db.execute("SELECT cash FROM users WHERE ID = ?", user_id) # :id and ? are the same
        # Get user-cash as a real number not a list or dict
        user_cash = user_cash_db[0]["cash"]

        # Confirm the user has enough shares
        user_shares_db = db.execute(
            "SELECT Shares FROM transactions WHERE User_id = ? and Symbol = ? GROUP BY Symbol", user_id, symbol)
        user_shares = user_shares_db[0]["Shares"]
        if user_shares < share:
            return apology("You don't have enough shares to sell")

        # compare user_cash with transaction_cost
        updated_cash = user_cash + transaction_cost
        db.execute("UPDATE users SET cash = ? WHERE id = ?", updated_cash, user_id)

        # Get date from datetime library
        date = datetime.datetime.now()

        # Insert transaction details into transaction table
        db.execute("INSERT INTO transactions (User_id, Symbol, Shares, Price, Date) VALUES (?,?,?,?,?)",
                   user_id, stock["symbol"], (-1) * share, stock["price"], date)

        # Return success text using flash function
        flash("TRANSACTION SUCCESSFUL! STOCK SOLD")

        return redirect("/")


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Show history of transactions"""
    if request.method == "POST":
        new_cash = int(request.form.get("new_cash"))

        user_id = session["user_id"]

        if not new_cash:
            return apology("You must input an amount")
        if new_cash <= 0:
            return apology("Invalid amount")

        user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_cash = user_cash_db[0]["cash"]

        updated_cash = new_cash + user_cash
        db.execute("UPDATE users SET cash\\ = ? WHERE id = ?", updated_cash, user_id)
        return redirect("/")
    else:
        return render_template("add.html")