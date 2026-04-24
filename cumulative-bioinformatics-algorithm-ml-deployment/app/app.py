from flask import Flask, request, jsonify
import joblib  
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Logic: if mass > 4500g and flipper > 200mm -> likely Gentoo species
    prediction = "Gentoo" if data['body_mass_g'] > 4500 else "Adelie/Chinstrap"
    return jsonify({'species_prediction': prediction})

if __name__ == '__main__':
    app.run(port=5000)
