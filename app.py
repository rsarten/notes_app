import sqlite3
from flask import Flask, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect("data/database.db")
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
app.config["SECRET_KEY"] = "this is the only secret left"

@app.route("/")
def index():
    conn = get_db_connection()
    notes = conn.execute("SELECT * FROM notes ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("index.html", notes = notes)

@app.route("/create", methods = ["GET", "POST"])
def create():
    if request.method == 'POST':
        content = request.form['content']
        if not content:
            flash("Note content is required!")
        
        else:
            conn = get_db_connection()
            conn.execute("INSERT INTO notes (content) VALUES (?)",
                            (content, ))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    
    return render_template("create.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')