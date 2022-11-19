# Used the following link as a tutorial to communicate User Info to python
# https://www.youtube.com/watch?v=6rPxwj1sR5c 

from flask import Flask, render_template, request, redirect, session
import json

app = Flask(__name__)


@app.route('/')
def query1filters():
    return render_template('query1filters.html')

@app.route('/processUserInfo/<string:userInfo>', methods=['POST'])
def processUserInfo(userInfo): 
    userInfo = json.loads(userInfo)
    print()
    print('USER INFO RECEIVED')
    print('--------------------')
    print(f"User Name: {userInfo['name']}")
    print(f"User Type: {userInfo['type']}")
    print()

    return 'Info Receieved Successfully'

if __name__ == '__main__':
    app.run(debug=True)