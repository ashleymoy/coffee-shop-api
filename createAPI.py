from flask import Flask, url_for, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/espresso', methods=['GET'])
def espresso():
    conn = sqlite3.connect('DrinkMenu.db')
    c = conn.cursor()
    espressoDrinks = c.execute('SELECT * FROM espresso').fetchall()
    return jsonify(espressoDrinks)

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
