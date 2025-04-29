import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

# Ensure directories exist
os.makedirs("data/raw", exist_ok=True)
os.makedirs("models", exist_ok=True)

# Load data
data_path = "data/raw/iris.csv"
if not os.path.exists(data_path):
    raise FileNotFoundError(f"Data file not found at {data_path}")

data = pd.read_csv(data_path)

# Preprocess
X = data.drop('species', axis=1)
y = LabelEncoder().fit_transform(data['species'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
model_path = "models/model.pkl"
joblib.dump(model, model_path)
from sklearn.metrics import classification_report
print(classification_report(y_test, model.predict(X_test)))
print(f"✅ Model saved as {model_path}")