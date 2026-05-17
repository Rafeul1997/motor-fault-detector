import pickle
import numpy as np
import os

# Load model from package
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)


def predict(features):
    """
    Predict motor condition

    Parameters:
        features (list): input feature values

    Returns:
        prediction result
    """

    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)

    return prediction[0]
