# -Build-a-REST-API-with-Flask
  Building a REST API with Flask

~This code creates a mini web API using the Flask framework.
It can:
  >Show all users
  >Add a new user
  >Update a user’s info
  >Delete a user

Flask — used to create the web app
request — lets the app read data sent from clients
jsonify — turns Python data into JSON format to send back as a response.

~Creating the app and storage
  -app = Flask(__name__)
   user_records = {}
    >app = Flask(__name__) sets up the web app.
    >user_records = {} is an empty dictionary that will store all users in memory.
    >Each user will look something like:    {  "1": {"name": "Alice", "email": "alice@gmail.com"}}

~Home route
  >@app.route("/")
  def home():
      return "<h2>✅ Flask API is running! Visit /users to view or manage users.</h2>"

  >When you open the main page (like http://127.0.0.1:5000/), it shows a simple HTML message confirming the API is working.

~View all users (GET)
  >If you go to /users with a GET request, it returns the list of all users in JSON format.
  >Add a new user (POST)
  >This route listens for a POST request at /users.
  >It reads the JSON data sent (like {"name": "John", "email": "john@gmail.com"}).
  >It automatically assigns an ID (like "1", "2", etc.).
  >It adds the new user to user_records.
  >Returns a success message and the newly added user

~Update an existing user (PUT)
  >This route updates an existing user’s data using a PUT request like /users/1.
  >If the user ID doesn’t exist, it returns a 404 error.
  >Otherwise, it updates only the provided fields (name or email).
  >Returns the updated user info.


~Delete a user (DELETE)
  >This listens for a DELETE request at /users/<user_id>.
  >If the user exists, it removes them from user_records.
  > Returns a message confirming deletion along with deleted user info.

~Running the app
  >debug=True means Flask will auto-restart when you make code changes.
  >This line starts the server on your computer (default: http://127.0.0.1:5000/).

