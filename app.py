from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

#Load Previously Trained Model
file = open("./model.pkl", 'rb')
model = pickle.load(file)

#Load 
data = pd.read_csv('./new_data.csv')
data.head()

@app.route('/')
def index():
    sex = sorted(data['sex'].unique())
    smoker = sorted(data['smoker'].unique())
    region = sorted(data['region'].unique())
    insurance_type = sorted(data['insurance_type'].unique())
    return render_template('index.html', sex= sex, smoker= smoker, region= region, insurance_type= insurance_type)

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form.get('age'))
    sex = request.form.get('sex')
    bmi = float(request.form.get('bmi'))
    children = int(request.form.get('children'))
    smoker = request.form.get('smoker')
    region = request.form.get('region')
    insurance_type = request.form.get('insurance_type')

    prediction = model.predict(pd.DataFrame([[age, sex, bmi, children, smoker, region, insurance_type]], 
                columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'insurance_type']))

    return str(prediction[0])           

if __name__=="__main__":
    app.run(debug=Fale,host='0.0.0.0',port=80)
