from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.predict import predict

# Initialize FastAPI app
app = FastAPI()

# Path to the trained model
MODEL_PATH = "models/model.pkl"


# Define the input data schema using Pydantic
class InputData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to MLOps API!"}


# GET endpoint for predict (informative only)



# POST endpoint for predictions
@app.post("/predict")
def make_prediction(input_data: InputData):
    try:
        # Prepare the input data for prediction
        data = [input_data.sepal_length, input_data.sepal_width, input_data.petal_length, input_data.petal_width]

        # Call the predict function with the input data and model path
        prediction = predict(data, MODEL_PATH)

        # Return the prediction result
        return {"prediction": prediction}
    except Exception as e:
        # Handle errors gracefully
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
