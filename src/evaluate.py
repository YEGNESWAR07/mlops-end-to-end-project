from sklearn.metrics import accuracy_score
import joblib

def evaluate(X_test, y_test, model_path):
    model = joblib.load(model_path)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    return acc
