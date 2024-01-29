# Import dependencies -- reuse code others have given us.
import sqlite3
import os
from markupsafe import escape
import datetime
from flask import Flask, render_template, request, url_for, redirect, abort, g

app = Flask("app")

# The database configuration
DATABASE = os.environ.get("FLASK_DATABASE", "app.db")


# Functions to help connect to the database
# And clean up when this application ends.
def get_db_connection():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


# Each @app.route(...) indicates a URL.
# Using that URL causes the function immediately after the @app.route(...) line to run.
# THIS ROUTE IS TO PROVE THE FLASK SETUP WORKS.
# YOU SHOULD REPLACE IT WITH YOUR OWN CONTENT.
@app.route("/")
def hello():
    """Return some friendly text."""
    return "Hello, World!"


### YOUR CODE GOES HERE ###
if __name__ == "__main__":
    app.run(debug=True)
