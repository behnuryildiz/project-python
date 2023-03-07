from flask import Flask, jsonify, request
import mysql.connector
from flask_restful import Resource, Api
from config import MYSQL_HOSTNAME, MYSQL_PORT, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE

app = Flask(__name__)
api = Api(app)

db = mysql.connector.connect()


# MySQL connection parameters
app.config['MYSQL_HOSTNAME'] = MYSQL_HOSTNAME
app.config['MYSQL_PORT'] = MYSQL_PORT
app.config['MYSQL_USERNAME'] = MYSQL_USERNAME
app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
app.config['MYSQL_DB'] = MYSQL_DATABASE



# Home Page 
@app.route("/")
def home():
    return "Welcome to my API!"

if __name__ == "__main__":
    app.run()

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


@app.route('/pets', methods=['GET'])
def get_pets():
    cursor = db.cursor()
    cursor.execute('SELECT pet_name, species FROM pets')
    pets = []
    for (pet_name, species) in cursor:
        pets = {'pet_name': pet_name, 'species': species}
        pets.append(pets)
    return jsonify(pets)

    
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
@app.route('/owners/<int:ownerId>', methods=['DELETE'])
def delete_owner(ownerId: int):
    cursor = db.cursor()
    cursor.execute('DELETE FROM owners WHERE ownerId = %s', (ownerId))

@app.route('/pets/<int:petId>', methods=['DELETE'])
def delete_pet(petId: int):
    cursor = db.cursor()
    cursor.execute('DELETE FROM pets WHERE petId = %s', (petId))


if __name__ == '__main__':
    app.run(debug=True)
