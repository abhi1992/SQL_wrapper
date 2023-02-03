import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(user='<username>', password='<password>', host='<hostname>', database='<database>')

# Define the query
query = "SELECT * FROM orders JOIN customers ON orders.customer_id = customers.id WHERE customers.city = 'San Francisco'"

# Execute the explain statement
cursor = cnx.cursor()
cursor.execute("EXPLAIN " + query)
explain_output = cursor.fetchall()

# Analyze the explain output
for row in explain_output:
    print(row)

# Make changes to the query based on the explain output
# ...

# Execute the optimized query and measure the performance
before_time = time.time()
cursor.execute(query)
results = cursor.fetchall()
after_time = time.time()
print('Query Execution Time:', after_time-before_time)

# Close the cursor and connection
cursor.close()
cnx.close()
