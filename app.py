from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
DATABASE = 'entries.db'

# Create the database table
with sqlite3.connect(DATABASE) as conn:
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS entries 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  email TEXT)''')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Insert the entry into the database
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('INSERT INTO entries (name, email) VALUES (?, ?)', (name, email))

    # Get all entries from the database
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM entries')
        entries = c.fetchall()

    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run()
