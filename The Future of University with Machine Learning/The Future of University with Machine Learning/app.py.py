import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)
#Import necessary libraries 
from tensorflow.keras.models import load_model
#model = pickle.load(open('university.pkl','rb))
model = load_model('model.h5')
@app.route('/') 
def home():
return render_template('Demo2.html')
@app.route('/y_predict',mtthods=['POST']) 
def y_predict():
#min max scaling
min1=[290.0, 92.0, 1.0, 1.8, 1.0, 6.8, 0.0]
max1=[348.0, 120.0, 5.0, 5.0, 5.0, 9.92, 1.0]
k= [float(x) for x in request.form.values()] 
P=[]
for i in range(7):
    l=(k[i]-min1[i])/(max1[i]-min1[i]) 
    p.append(l)
prediction = model.predict([p]) 
print(prediction)
output-prediction[0] 
if(output=False):
    return render_template('nochance.html', prediction_text='You Dont have a chance of getting')
else:
   return render_template('chance.html', prediction text="You have a chance of getting admis')
if __name__ == "__main__":
    app.run(debug=False)
