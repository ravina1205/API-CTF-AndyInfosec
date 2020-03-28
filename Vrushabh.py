
from flask import Flask


app = Flask(__name__)

@app.route("/")

def dummy_api():


    return ("I'm Vrushabh"), 200
@app.route("/help")
def help():
    return ("Help is here")
if __name__ == "__main__":
    app.run()

