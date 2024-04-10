# Home Sale Price Prediction

## Description
This project focuses on predicting home sale prices using a model trained with Azure Machine Learning (Azure ML). The model leverages historical data on home sales, including features like square footage, year built, number of bedrooms, and other relevant attributes to predict sale prices of homes.

## Getting Started

### Dependencies
- Python 3.9 or higher
- pandas
- numpy
- joblib
- scikit-learn
- Azure ML SDK for model deployment and management (optional for local runs)
  
Ensure you have Miniconda or Anaconda installed to manage the environment and dependencies.

### Installing
1. Clone this repository to your local machine.
2. Use the provided `environment.yml` file to create a Conda environment:
    ```bash
    conda env create -f environment.yml
    ```
3. Activate the environment:
    ```bash
    conda activate project_environment
    ```

### Executing Program
1. Ensure the model (`model.pkl`) and the environment file (`environment.yml`) are placed in the root directory.
2. Prepare your test dataset in a CSV format and ensure it matches the schema used during model training.
3. Run the prediction script:
    ```bash
    python run_prediction.py
    ```
4. The script will output predictions in a CSV file named `predicted_sold_prices.csv` in the root directory.

## Model Information
- **Training Data:** The model was trained on a dataset comprising various features like home size, location, age, etc.
- **Algorithm:** The model is an ensemble of various algorithms optimized by Azure AutoML to predict sale prices as accurately as possible.
- **Performance:** The model's performance metrics (e.g., RMSE, MAE) are documented in the model training logs.
