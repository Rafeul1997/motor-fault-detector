from motor_fault import predict

# Example input (CHANGE based on your dataset)
sample = [0.5, 1.2, 0.7, 2.0] # [voltage, current, speed, temperature]

result = predict(sample)

print("🔍 Prediction Result:", result)
