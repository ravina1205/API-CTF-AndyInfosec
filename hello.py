from flask import Flask

app = Flask(__name__)

@app.route("/v1/CTF")
def helloWorld():
	return "^^FLAG^^\n"

if __name__ == '__main__':
	app.run(port=8080)
