# Air Quality Prediction Project

## Overview

This project focuses on predicting air quality using machine learning algorithms. After evaluating various models, Random Forest and K-Nearest Neighbours (KNN) were selected for their superior performance in accuracy, precision, recall, and F1-score. An ensemble model combining these two algorithms was implemented for real-time air quality prediction, and a user-friendly web interface was created using Flask.

## Data Pre-processing

In Python, I undertook several key steps to prepare the data for analysis:

1. **Loading Data:** Loaded the preprocessed data from a CSV file.
2. **Calculating Averages:** Computed the mean values for `NO2_MAX` and `NO2_MIN`, creating a new column `NO2_mean`.
3. **Removing Old Columns:** Removed the original `NO2_MAX` and `NO2_MIN` columns.
4. **Handling Other Pollutants:** Calculated mean values for `PM10_MAX`, `PM10_MIN`, `PM2_MAX`, `PM2_MIN`, `SO2_MAX`, and `SO2_MIN`, added corresponding mean columns, and removed the original columns.
5. **Final Adjustments:** Similar steps were taken for `CO_MAX`, `CO_MIN`, `CO2_MAX`, and `CO2_MIN`, calculating their means and removing the original columns.

## Model Evaluation

I evaluated several machine learning models and their performance was measured based on accuracy, precision, recall, and F1-score:

1. **Random Forest:** Achieved perfect scores across all metrics (accuracy, precision, recall, F1-score), making it the most reliable model for air quality prediction.
2. **Support Vector Machine (SVM):** Delivered strong performance with an accuracy of 0.963 and good precision, recall, and F1-scores. While not perfect, it demonstrated reliable predictions.
3. **K-Nearest Neighbours (KNN):** Performed exceptionally well, with accuracy near 1.0 and high scores in precision, recall, and F1-score, proving effective for accurate predictions.

Based on these results, I employed an ensemble approach combining Random Forest and KNN for the final prediction model.

## Real-Time Prediction

### Ensemble Model

I implemented an ensemble model that combines the Random Forest and KNN algorithms. This approach leverages the strengths of both models, improving overall prediction performance and ensuring more accurate and reliable real-time air quality predictions.

### Flask for GUI

I used **Flask**, a Python web framework, to develop a simple and intuitive web-based interface. Users can input air quality parameters, and the system will provide real-time predictions based on the ensemble model.

### HTML for Layout

The graphical interface was structured using **HTML** to create a clean and interactive environment. The web pages feature input fields for air quality parameters and sections for displaying prediction results.

### Implementation Details

- The ensemble model is saved using `joblib`, which is loaded during the Flask application runtime.
- Flask routes are defined for rendering the home page and handling prediction logic.
- HTML templates, particularly `index.html`, are designed to provide a user-friendly layout and styling for the GUI.

## Evaluation Metrics

The ensemble model demonstrated outstanding performance across all metrics, providing the following results:

| Metric         | Mean Value |
|----------------|------------|
| **Accuracy**   | 0.9996     |
| **Precision**  | 0.9993     |
| **Recall**     | 0.9998     |
| **F1-score**   | 0.9995     |

## Why Random Forest and KNN?

Random Forest and KNN were chosen for their consistent high performance in air quality prediction tasks. During the evaluation phase, both models outperformed other machine learning algorithms, and their ensemble further enhanced prediction accuracy.

## Features (X) and Target (y)

- **X (Features):** `NO2_mean`, `PM10_mean`, `PM2_mean`, `SO2_mean`, `CO_mean`, `CO2_mean`
- **y (Target):** `Air_Quality`

## Conclusion

By combining the strengths of Random Forest and KNN in an ensemble model and providing a user-friendly real-time prediction interface, this project offers a robust solution for air quality prediction. The high performance of the model across all key metrics ensures that it can be relied upon for accurate and timely predictions.

