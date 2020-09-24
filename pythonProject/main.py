from flask import Flask, request
from handler.UsersHandler import UsersHandler

from flask_cors import CORS

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    return 'Hello, this is the Matchware App!'

@app.route('/user', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UsersHandler().insertUserJson(request.json)
    else:
        if not request.args:

            return UsersHandler().getAllUsers()
        else:
            return UsersHandler().serachUser(request.args)



if __name__ == '__main__':
    app.run()