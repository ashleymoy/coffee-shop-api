import sqlite3

# create connection
conn = sqlite3.connect("DrinkMenu.db")

c = conn.cursor()

# create table
c.execute("CREATE TABLE IF NOT EXISTS espresso(name TEXT " +
                                    "PRIMARY KEY,tall REAL)")

espressoDrinkNames = ['Cappuccino', 'Caffe Latte', 'Caffe Americano', 'Espresso', 'Espresso Macchiato', 'White Chocolate Mocha', 'Caramel Macchiato']
tallPrices = [2.95, 2.95, 2.25, 1.95, 2.05, 3.95, 3.95]

# insert data 
for i in range(0,6):
    c.execute("INSERT INTO espresso (name,tall) "+
                "VALUES (?,?)",(espressoDrinkNames[i],tallPrices[i]))

conn.commit()
c.close()
conn.close()
