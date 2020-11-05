from flask import Flask, request
from handler.UsersHandler import UsersHandler
from handler.ProjectHandler import ProjectHandler
from handler.PostHandler import PostHandler
from handler.CredentialHandler import CredentialHandler
from handler.MemberHandler import MemberHandler
from handler.MessagesHandler import MessagesHandler
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
            print("Here")
            return UsersHandler().getAllUsers()

@app.route('/message',methods=['GET','POST'])
def messages():
    if request.method == 'POST':
        return MessagesHandler().insertMessageJson(request.json)
    else:
        if request.args:
            return MessagesHandler().getMessages(request.args)



@app.route('/project', methods=['GET', 'POST'])
def project():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ProjectHandler().insertProjectJson(request.json)
    else:
        if not request.args:
            return ProjectHandler().getAllProjects()


@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PostHandler().insertPostJson(request.json)
    else:
        if not request.args:
            return PostHandler().getAllPosts()


@app.route('/members', methods=['GET', 'POST'])
def members():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return MemberHandler().insertMemberJson(request.json)
    else:
        if not request.args:
            return MemberHandler().getAllMembers()


@app.route('/credentials', methods=['GET', 'POST'])
def credentials():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return CredentialHandler().insertCredentialJson(request.json)
    else:
        if not request.args:
            return CredentialHandler().getAllCredentials()


if __name__ == '__main__':
    app.run()
