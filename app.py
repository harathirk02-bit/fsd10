from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "ML API Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    data = list(map(float, data))
    prediction = model.predict([data])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)