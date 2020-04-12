from flask import Flask

app = Flask(__name__)

@app.route("/healthCheck")
def healthCheck():
	return "200 Ok"

@app.route("/login/<uname>/<passwd>")
def login(uname=None,passwd=None):
    users =[
      {
      'username':'Adarsh','password':'Apple1'
    },{
      'username':'vrushabh','password':'Apple2'
    },{
      'username':'prateek','password':'Apple3'
    },{
      'username':'prerana','password':'Apple4'
    },{
      'username':'Andy','password':'Apple5'
    }
    ]
    for user in users:
      if (uname == user['username'] and passwd == user['password']):
        return "Logged In as %s " % uname
      
    
    return "Login Failed"
    # # if (uname == 'Adarsh'):
    # return 'your name is %s' % uname

if __name__ == '__main__':
	app.run(port=8181)