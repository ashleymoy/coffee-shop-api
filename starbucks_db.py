import sqlite3

# create connection
conn = sqlite3.connect("DrinkMenu.db")

c = conn.cursor()
'''
# create table
c.execute("CREATE TABLE IF NOT EXISTS espresso(name TEXT " +
                                    "PRIMARY KEY, small REAL, medium REAL, large REAL)")

espressoName = ['Cappuccino', 'Caffe Latte', 'Caffe Americano', 'Espresso', 'Espresso Macchiato', 'White Chocolate Mocha', 'Caramel Macchiato']
smallPrices = [2.95, 2.95, 2.25, 1.95, 2.05, 3.95, 3.95]
mediumPrices = [3.65, 3.65, 2.65, 2.45, 2.45, 5.45, 4.45]
largePrices = [4.25, 4.45, 3.25, 2.55, 2.55, 4.95, 4.95]

# insert data
for i in range(0,6):
    c.execute("INSERT INTO espresso (name, small, medium, large) "+
                "VALUES (?,?,?,?)",(espressoName[i], smallPrices[i], mediumPrices[i], largePrices[i]))
'''
# create table
c.execute("CREATE TABLE IF NOT EXISTS coffee_and_tea(name TEXT " +
                                    "PRIMARY KEY, small REAL, medium REAL, large REAL)")

coffee_and_tea_name = ['Coffee', 'Iced Coffee', 'Hot Chocolate', 'Iced Tea', 'Iced Tea Lemonade', 'Chai Tea Latte']
smallPrices = [1.95, 2.45, 2.75, 1.95, 2.65, 3.45]
mediumPrices = [2.10, 2.75, 3.25, 2.45, 3.25, 4.15]
largePrices = [3.45, 2.95, 3.45, 2.75, 3.65, 4.45]

# insert data
for i in range(0,5):
    c.execute("INSERT INTO coffee_and_tea (name, small, medium, large) "+
                "VALUES (?,?,?,?)",(coffee_and_tea_name[i], smallPrices[i], mediumPrices[i], largePrices[i]))

conn.commit()
c.close()
conn.close()
