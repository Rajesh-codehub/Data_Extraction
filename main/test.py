import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rajubay@123",
  database="test"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a SELECT query
mycursor.execute("SELECT * FROM people")

# Fetch all rows
myresult = mycursor.fetchall()

# Print the results
for row in myresult:
    print(row)

# Close the cursor and connection
mycursor.close()
mydb.close()