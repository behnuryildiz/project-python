from flask import Flask, jsonify, request
import mysql.connector
from flask_restful import Resource, Api
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

app = Flask(__name__)
api = Api(app)

db = mysql.connector.connect()


# MySQL connection parameters
app.config['MYSQL_HOST'] = MYSQL_HOST
app.config['MYSQL_PORT'] = MYSQL_PORT
app.config['MYSQL_USER'] = MYSQL_USER
app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
app.config['MYSQL_DB'] = MYSQL_DATABASE



# Endpoint to retrieve all owners
@app.route('/owners', methods=['GET'])
def get_owners():
    cursor = db.cursor()
    cursor.execute('SELECT first_name, last_name, email FROM owners')
    owners = []
    for (first_name, last_name, email) in cursor:
        user = {'first_name': first_name, 'last_name': last_name, 'email': email}
        owners.append(owners)
    return jsonify(owners)

# Endpoint to add a new owner
@app.route('/owners/add', methods=['POST'])
def add_owners():
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    email = data ['email']
    cursor = db.cursor()
    cursor.execute('INSERT INTO owners (first_name, last_name, email) VALUES (%s, %s, %s)', (first_name, last_name, email))
    db.commit()
    return jsonify({'message': 'Owner added successfully'})

# Endpoint to delete a user by ID
@app.route('/owners/<int:first_name>', methods=['DELETE'])
def delete_owner(first_name):
    cursor = db.cursor()
    cursor.execute('DELETE FROM owners WHERE first_name = %s', (user_id))


if __name__ == '__main__':
    app.run(debug=True)
