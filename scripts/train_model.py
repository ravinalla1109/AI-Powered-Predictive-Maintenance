import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_model(data_path, model_path):
    """Train a predictive maintenance model."""
    data = pd.read_csv(data_path)
    X = data.drop("failure", axis=1)  # Features
    y = data["failure"]  # Target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    predictions = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, predictions))
    print("Classification Report:\n", classification_report(y_test, predictions))

    # Save the model
    joblib.dump(model, model_path)

if __name__ == "__main__":
    train_model("../data/processed_data.csv", "../models/predictive_model.pkl")
