import numpy as np
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load trained model
saved_model = r"D:\python\weather\model.pkl"
with open(saved_model, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read input values from form
        month = int(request.form.get('month'))
        precipitation = float(request.form.get('precipitation'))
        temp_max = float(request.form.get('temp_max'))
        temp_min = float(request.form.get('temp_min'))
        wind = float(request.form.get('wind'))

        # Prepare input array
        input_data = np.array([[month, precipitation, temp_max, temp_min, wind]])

        # Predict
        predictions = model.predict(input_data)

        if predictions[0] == 0:
            result="Rainy"
        elif predictions[0] == 1:
            result = "Cloudy"
        else:
            result = "Sunny"

        return render_template('index.html',month=month,precipitation=precipitation,temp_max=temp_max,temp_min=temp_min,wind=wind, result=result,submit=True)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
