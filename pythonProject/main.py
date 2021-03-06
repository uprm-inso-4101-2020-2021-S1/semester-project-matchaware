from flask import Flask, request
from handler.UsersHandler import UsersHandler
from handler.ProjectHandler import ProjectHandler
from handler.PostHandler import PostHandler
from handler.CredentialHandler import CredentialHandler
from handler.MemberHandler import MemberHandler
from handler.MessagesHandler import MessagesHandler
from handler.CommentHandler import CommentsHandler
from handler.ImagesHandler import ImagesHandler
from flask_cors import CORS


# Activate
app = Flask(__name__)
#app = Flask(__name__, static_folder='../build', static_url_path='/')
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    return 'Hello, this is the Matchware App!'
    #return app.send_static_file('index.html')



@app.route('/user', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UsersHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return UsersHandler().getAllUsers()

@app.route('/UserSignUp', methods=['POST'])
def UserSignUp():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UsersHandler().insertUserSignUpJson(request.json)
    else:
        if not request.args:
            return UsersHandler().getAllUsers()

#For getting user information by ID. Used in the User Home page
@app.route('/uid/<int:userid>', methods=['GET'])
def usersByID(userid):
    if request.method == 'GET':
            return UsersHandler().getUserById(userid)

@app.route('/credentials', methods=['GET', 'POST'])
def credentials():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return CredentialHandler().insertCredentialLGPageJson(request.json)
    else:
        if not request.args:
            return CredentialHandler().getAllCredentials()

@app.route('/CredSignUp', methods=['POST'])
def credSignUp():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return CredentialHandler().insertCredentialLGPageJson(request.json)
    else:
        if not request.args:
           return "Incorrect argument."

#The Login page check for user. Returns UserID in a json file.
@app.route('/creds/logcheck', methods=['GET'])
def getCredentialbyUsernameandPassword(username, password):
    if request.method == 'POST':
        return CredentialHandler().getCredentialByUsernameandPassword(username, password)
    else:
        if not request.args:
            return CredentialHandler().getAllCredentials()


@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'POST':
        return MessagesHandler().insertMessageJson(request.json)
    else:
        if not request.args:
            print("Here")
            return MessagesHandler().getAllMessagess()


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


@app.route('/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return CommentsHandler().insertCommentJson(request.json)
    else:
        if not request.args:
            return CommentsHandler().getAllComments()


@app.route('/images', methods=['GET', 'POST'])
def images():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ImagesHandler().insertImageJson(request.json)
    else:
        if not request.args:
            return ImagesHandler().getAllImages()


if __name__ == '__main__':
    app.run()
