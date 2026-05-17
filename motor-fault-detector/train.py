import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle
import os

# Load dataset
df = pd.read_csv("data/im_data.csv")

# CHANGE 'label' to your actual target column name
X = df.drop("label", axis=1)
y = df["label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = SVC()
model.fit(X_train, y_train)

# Save model inside package folder
os.makedirs("motor_fault", exist_ok=True)

with open("motor_fault/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to motor_fault/model.pkl")
