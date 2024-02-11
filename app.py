# Import dependencies -- reuse code others have given us.
import sqlite3
import os
import datetime
from flask import Flask, jsonify, render_template, request, url_for, redirect, abort, g
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'app.db')
app.config["DATABASE"] = db_path#这里db_path为绝对路径

# The database configuration
DATABASE = os.environ.get("FLASK_DATABASE", "app.db")


# Functions to help connect to the database
# And clean up when this application ends.
def get_db_connection():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(app.config["DATABASE"])
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
@app.route("/index/")
def main():
    return render_template("goose.html")

@app.route("/goose", methods=["POST"])
def search():
    data = request.get_data()
    json_data = json.loads(data)
    # print(json_data)
    searchInput = json_data.get("searchInput")
    lowSearchInput = searchInput.lower() # turn input into lowercase letters to match dishes in the menu table
    
    conn = get_db_connection()
    searchRe = conn.execute('SELECT * FROM menu WHERE name LIKE ?',('%'+ lowSearchInput + '%',)).fetchall() # type is list.
    conn.commit()
    conn.close()
    if not searchRe:
        print('cannot find any relevant food')
    # print("select successfully")
    return searchRe


@app.route("/order", methods=["POST"])
def order():
    data = request.get_data()
    # print(data)
    json_data = json.loads(data)
    # print(json_data)
    qu = json_data.get("quantity")
    qu_int = int(qu)
    
    conn = get_db_connection()
    dishRecord = conn.execute('SELECT quantity FROM menu WHERE id = 1').fetchone() # type is tuple and length is 1.
    info = dict()
    if qu_int <= dishRecord[0]:    
        conn.execute('INSERT INTO customer_orders (customer_id, dishes_id, quantity) VALUES (?,?,?)',('',1,qu_int))
        conn.commit()
        info['status'] = 'success'
        info['info'] = 'order successfully!'
        order_id = conn.execute('SELECT last_insert_rowid() FROM customer_orders').fetchone()
        conn.commit()
        info['order_id'] = order_id[0]
        # print(info['order_id'])
        conn.execute('UPDATE menu SET quantity = ? WHERE id = 1', (dishRecord[0] - qu_int,))
        conn.commit()
        conn.close()
        # print("insert successfully")
    else:
        info['status'] = 'error',
        info['info'] = 'the quantity is over stock!'
        info['order_id'] = ''
    return jsonify(info)

@app.route("/login", methods=["POST"])
def login():
    # print("login")
    data = request.get_data()
    # print(data)
    json_data = json.loads(data)
    # print(json_data)
    email = json_data.get("loginEmail")
    password = json_data.get("loginPassword")

    info = dict()
    conn = get_db_connection()
    userRecord = conn.execute('SELECT * FROM user WHERE email = ?',(email,)).fetchall() # type is list and length is 1.
    if len(userRecord) == 1:
        for i in userRecord: # i is tuple. i[0] is id, i[1] is email, i[2] is password.
            userPassword = i[2]
        if userPassword == password:
            info["status"] = 'success'
            info["info"] = 'login successfully!'
        else:
            info["status"] = 'error'
            info["info"] = 'password is wrong!' 
    else:
        info["status"] = 'error'
        info["info"] = "email address doesn't exist!" 
    
    conn.commit()
    conn.close()
    # print("select successfully")
    return jsonify(info)

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_data()
    # print(data)
    json_data = json.loads(data)
    # print(json_data)
    email = json_data.get("regEmail") # type is str
    
    info = dict()
    conn = get_db_connection()
    userRecord = conn.execute('SELECT * FROM user WHERE email = ?',(email,)).fetchall() # type is list and length is 1.
    if not userRecord: # 如果userRecord为空
        conn.execute("INSERT INTO user (email, password) VALUES (?,?)", (
            json_data.get('regEmail'),
            json_data.get('regPassword'),
            )
        )
        info['status'] = 'success'
        info["info"] = 'sign up successfully!'
        conn.commit()
        conn.close()
        # print("insert successfully")
    else:
        info['status'] = 'error'
        info["info"] = 'email address already exists!'
   
    return jsonify(info)



if __name__ == "__main__":
    app.run(port=8899, debug=True)
