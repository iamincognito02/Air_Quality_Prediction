from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('phase2_ensemble_model.pkl')

# Define the route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Define the route for model prediction
@app.route("/", methods=["POST"])
def predict():
    # Get data from the HTML form
    feature1 = float(request.form["feature1"])
    feature2 = float(request.form["feature2"])
    feature3 = float(request.form["feature3"])
    feature4 = float(request.form["feature4"])
    feature5 = float(request.form["feature5"])
    feature6 = float(request.form["feature6"])

    # Create a DataFrame from the input data
    input_data = pd.DataFrame(
        [[feature1, feature2, feature3, feature4, feature5, feature6]],
        columns=[
            "NO2_mean",
            "PM10_mean",
            "PM2_mean",
            "SO2_mean",
            "CO_mean",
            "CO2_mean",
        ],
    )

    # Predict using the model
    prediction = model.predict(input_data)

    # Convert prediction to string for displaying
    prediction_str = " ".join(prediction)

    return render_template("index.html", prediction=prediction_str)


if __name__ == "__main__":
    app.run(debug=True)

