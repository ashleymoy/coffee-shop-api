from flask import Flask, url_for, jsonify
import sqlite3, logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

application = Flask(__name__)

@application.route('/')
def welcome():
    return 'Welcome to the coffee shop.'

@application.route('/menu/<drinks>', methods=['GET'])
def show_drinks(drinks):
    # show the menu items for that section
    conn = sqlite3.connect('DrinkMenu.db')
    c = conn.cursor()
    menuItems = c.execute('SELECT * FROM ' + str(drinks)).fetchall()
    return jsonify(menuItems)

@application.errorhandler(404)
def page_not_found(error):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# run application
if __name__ == '__main__':
    application.run()
