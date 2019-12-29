import sqlite3

# create connection object
conn = sqlite3.connect("Training.db")

c = conn.cursor()

# execute method does stuff with databases, generally. the arg is a SQL command
c.execute("CREATE TABLE IF NOT EXISTS iceCubeMelting(time INT " +
                                    "PRIMARY KEY,temperature REAL, date TEXT)")

# insert data into table
#c.execute("INSERT INTO iceCubeMelting VALUES (0,27.0,"28-08-2017")")

# insert more data dynamically. specify the columns that you're inserting
#for i in range(1,5):
    # c.execute("INSERT INTO iceCubeMelting (time,temperature,date) "+
                #"VALUES (?,?,?)",(i,27-0.1*i,"28-09-2017"))

#for i in range(5,8):
    #c.execute("INSERT INTO iceCubeMelting (time,temperature) "+
                #"VALUES (?,?)",(i,27-0.1*i))

# this removes a table and all its data
#c.execute("DROP TABLE iceCubeMelting")

# get info from table. you can save it as a list to a variable
# c.execute("SELECT time FROM iceCubeMelting")
# c.execute("SELECT * FROM iceCubeMelting")

# select 2 rows starting at index 3
c.execute("SELECT * FROM iceCubeMelting LIMIT 2 OFFSET 3")
data = c.fetchall()

#fetch first result in query
# result = c.fetchone()

# updates database with info. use commit method when inserting data or deleting, etc.
# conn.commit()

# close cursor and db connection
c.close()
conn.close()
