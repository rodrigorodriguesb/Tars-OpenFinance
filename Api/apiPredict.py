import numpy as np
import os
from flask import Flask, request, render_template, make_response
from sklearn.extendels import joblib 

app = Flask(__name__, static_url_path='*/static')
model = joblib.load('[nosso aquivo]')

app.route('/')
def display_gui():
    return render_template('template.html')


@app.route('[nosso_endpoint]', methods=['POST'])

def verificar():
    classe = model.predict(teste)[0]
    print("Classe predita: {}".format(str(classe)))


if __name__ == "__main__":
    port = int(os.environ.get('PORT',5500))
    app.run(host='0.0.0.0', port=port)




