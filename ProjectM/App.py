from flask import Flask,request,render_template
app = Flask(__name__,template_folder="Flask")

@app.route('/')
def home():
	return render_template('App.html')

def get_prediction(n1):
	import pickle
	import os
	p = os.path.dirname(__file__)
	filepath = os.path.join(p,'model.data')
	rf = pickle.load(open(filepath,'rb'))
	y_predict = rf.predict([[n1]])
	return y_predict[0]

@app.route('/calc',methods=['get','post'])
def calc():
	MSRP = request.form['Engine HP']
	p = get_prediction( int(MSRP))
	return  "Answer " + str(p)

if __name__ == "__main__":
    print("Starting Python Flask Server For Car Prediction...")
    app.run(debug=True)
  
