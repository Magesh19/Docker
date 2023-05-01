from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
mydb = mysql.connector.connect(
  host="db",
  user="user",
  password="example",
  database="covid"
)

# Define route for handling user input
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        regno = request.form["regno"]
        cursor = mydb.cursor()
        cursor.execute("SELECT vaccinated FROM students WHERE regno=%s", (regno,))
        result = cursor.fetchone()
        if result:
            return "Vaccination Status: {}".format(result[0])
        else:
            return "No record found for registration number {}".format(regno)
    return '''
        <form method="post">
            Registration Number: <input type="text" name="regno" required>
            <input type="submit" value="Check">
        </form>
    '''

if __name__== "_main_":
    app.run(host="0.0.0.0", port=5000,debug=True)