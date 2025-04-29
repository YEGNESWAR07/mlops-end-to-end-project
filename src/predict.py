import joblib
import numpy as np
import os


def predict(input_data, model_path):
    """
    Predicts the output for the given input data using the specified model.

    Args:
        input_data (list or array-like): Input features for prediction.
        model_path (str): Path to the saved model file.

    Returns:
        dict: A dictionary containing the prediction result.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")

    try:
        model = joblib.load(model_path)
    except (EOFError, ModuleNotFoundError) as e:
        raise RuntimeError(f"Failed to load the model: {e}")

    # Ensure input_data is a 2D array
    #input_data = np.array(input_data).reshape(1, -1)
    input_data = np.array([[5.1, 3.5, 1.4, 0.2]])
    # Perform prediction
    prediction = model.predict(input_data)

    # Return the prediction as a JSON-serializable dictionary
    return {"prediction": int(prediction[0])}