from flask import Flask, request, redirect, render_template
import sqlite3
import string
import random

app = Flask(__name__)

# Database setup
def init_db():
    with sqlite3.connect('urls.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, original_url TEXT, short_url TEXT)')
    conn.close()

# Generate a random string for the short URL
def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Add URL to the database
def add_url(original_url):
    short_url = generate_short_url()
    with sqlite3.connect('urls.db') as conn:
        conn.execute('INSERT INTO urls (original_url, short_url) VALUES (?, ?)', (original_url, short_url))
    return short_url

# Get original URL from the database
def get_original_url(short_url):
    with sqlite3.connect('urls.db') as conn:
        cursor = conn.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_url,))
        row = cursor.fetchone()
    return row[0] if row else None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_url = add_url(original_url)
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    original_url = get_original_url(short_url)
    if original_url:
        return redirect(original_url)
    return "URL not found", 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
