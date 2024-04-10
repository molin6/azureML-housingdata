import pandas as pd
import joblib

# Initialize and load the model
def init():
    model_path = 'model.pkl'  # Update this path if your model is located elsewhere
    try:
        print("Loading model from path.")
        model = joblib.load(model_path)
        print("Loading successful.")
        return model
    except Exception as e:
        print(e)
        raise

# Predict function
def run(data, model):
    # Ensure 'Horses' column is correctly formatted as boolean
    if 'Horses' in data.columns:
        data['Horses'] = data['Horses'].map({'Y': True, 'N': False})
        # Optional: Handle NaN values if any. Here we fill NaNs with False.
        data['Horses'] = data['Horses'].fillna(False)
    
    # Drop the 'sold_price' column if it exists
    if 'sold_price' in data.columns:
        data = data.drop(columns=['sold_price'])
    
    result = model.predict(data)
    return result

# Main execution
if __name__ == "__main__":
    # Load the test data
    test_data = pd.read_csv('officialtestdata.csv')  # Update this path if necessary
    
    # Initialize the model
    model = init()
    
    # Make predictions
    predictions = run(test_data, model)
    
    # Save predictions to CSV
    predictions_df = pd.DataFrame(predictions, columns=['Predicted_Sold_Price'])
    predictions_df.to_csv('predicted_sold_prices.csv', index=False)
    print("Predictions saved to predicted_sold_prices.csv")
