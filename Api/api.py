import pandas as pd
from flask import Flask, request
import pickle

modelo = pickle.load( open('ineligenciaDecisionTree.pkl', 'rb'))
MinMa = pickle.load( open('MinMax.pkl', 'rb'))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if data:
        if isinstance( data, dict):
            data_row = pd.DataFrame(data, index=[0])
            print("if")
        else:
            print("else")
            data_row = pd.DataFrame( data, columns=data[0].keys())
    # norm = MinMa.transform(X=data_row)
    pred = modelo.predict(data_row)
    data_row['outlier'] = pred

    resumo = data_row.to_json( orient='records')


    return data_row.to_json( orient='records')



if (__name__ == '__main__'):
    app.run(host='0.0.0.0',port='5000')
    print("rodei")
