# importing the necessary tools
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():

    connection = sqlite3.connect('MyData.db')
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    connection.close()
    app.logger.info(users)  # Log the items fetched from the database
    return render_template('index.html', users=users)

# connecting the database to this python program
connection = sqlite3.connect('MyData.db')


# est connection with database cursor to make chnages
cursor = connection.cursor()

# creating a table in the database for users
# each user has a name (text type), id (integer type), and points (integer type)
#cursor.execute('CREATE TABLE users(name TEXT, id INTEGER, points INTEGER)')


# commiting those changes to the database
connection.commit()




@app.route('/add', methods= ['POST'])
def add_item():
    name = input("Please enter the user's name: ")
    user_id = int(input("Please enter the user's id: "))
    points = int(input("Please enter the user's points: "))

    # connecting the database to this python program
    connection = sqlite3.connect('MyData.db')


    # est connection with database cursor to make changes
    cursor = connection.cursor()


    cursor.execute("INSERT INTO users VALUES (?,?,?)" (name, user_id, points))

    # commiting the changes and closing the connection
    connection.commit()
    connection.close()



# method for searching for a user by user id
@app.route('/search', methods=['GET'])
def search_name():
    # asking for user id number to search
    search = int (input("Enter a user's name to search: "))

    # connecting the database to this python program
    connection = sqlite3.connect('MyData.db')


    # est connection with database cursor to make chnages
    cursor = connection.cursor()


    # searching the entire db for user unique id number
    cursor.execute('SELECT * FROM users WHERE id LIKE ?', (search))
    items = cursor.fetchall()
    connection.close()
    #return render_template('search.html', items=items)



# function to delete user in db
@app.route('/delete', methods=['GET'])
def delete_item(item_id):


    # connecting the database to this python program
    connection = sqlite3.connect('MyData.db')


    # est connection with database cursor to make chnages
    cursor = connection.cursor()


    # using the user id value to find and delete user from db
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))

    # commiting the changes and closing the connection
    connection.commit()
    connection.close()


