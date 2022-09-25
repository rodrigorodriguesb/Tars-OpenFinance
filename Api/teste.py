import pandas as pd
from Flask import Flask

modelo = pickle.load( open('../inteligencia.pkl', 'rb'))

Flask(__name__)

@app.route(/predict, methods=['POST'])
def predict():
    data = request.get_json()

    if data:
        if instance( data, dict):
            data_row = pd.DataFrame(data, index[0])
        else:
            data_row = pd.DataFrame( data, columns=data[0].keys)

    pred = modelo.predict(data_row)
    data_row['prediction'] = pred

    return data_row.to_json( orient='records')



if __name__ === '__main__':
    app.run(host='0.0.0.0',port='5000')