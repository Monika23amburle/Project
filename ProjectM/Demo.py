from flask import Flask,render_template,request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('Demo.html'
@app.route('/')
def home():
	return "Hello,welcome to my home webpage.";

)

if __name__ == "__main__":
	app.run()


    

