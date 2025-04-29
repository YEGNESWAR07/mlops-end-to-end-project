from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess(data):
    X = data.drop('species', axis=1)
    y = LabelEncoder().fit_transform(data['species'])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
