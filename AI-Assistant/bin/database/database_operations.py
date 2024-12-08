import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="aiapplication"  # Make sure to specify the database
    )
    print("Connection made to Database!")
    cursor = con.cursor()

    # Function to insert login credentials into the database
    def insert_login(username, password):
        try:
            query = "INSERT INTO login (username, password) VALUES (%s, %s)"
            values = (username, password)
            cursor.execute(query, values)
            con.commit()  # Commit the changes
            print(f"Login credentials for {username} saved!")
        except mysql.connector.Error as err:
            print(f"Error occurred during insert: {err}")

except mysql.connector.Error as err:
    print(f"An error occurred: {err}")
