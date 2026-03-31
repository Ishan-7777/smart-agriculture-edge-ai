
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

# 1. Setup Paths
base_dir = os.path.dirname(os.path.dirname(__file__)) # Project Root
data_path = os.path.join(base_dir, 'data', 'sensor_data.csv')
model_dir = os.path.join(base_dir, 'models')

if not os.path.exists(model_dir):
    os.makedirs(model_dir)

print("🚀 Loading Data for TinyML Training...")
data = pd.read_csv(data_path)

# 2. Preprocessing
# Inputs: Moisture, Temp, Humidity, pH
X = data[['Soil_Moisture', 'Temperature', 'Humidity', 'pH_Level']]
# Output: Crop_Status (0 or 1)
y = data['Crop_Status']

# Split into Training and Testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data (Neural Networks like numbers between 0 and 1)
# NOTE: In a real edge device, you'd need to do this math manually on the chip.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Build the Neural Network
# We make it "Tiny" (small number of neurons)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(4,)), # Input Layer
    tf.keras.layers.Dense(8, activation='relu'),                    # Hidden Layer
    tf.keras.layers.Dense(1, activation='sigmoid')                  # Output Layer (Prob between 0 and 1)
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 4. Train the Model
print("🧠 Training Neural Network...")
model.fit(X_train_scaled, y_train, epochs=20, batch_size=16, verbose=1)

# Evaluate
loss, accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"✅ Training Complete. Model Accuracy: {accuracy * 100:.2f}%")

# 5. Convert to TinyML Format (TensorFlow Lite)
# This step satisfies Unit I requirements
print("📉 Converting to TinyML (.tflite)...")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# 6. Save the Model
tflite_path = os.path.join(model_dir, 'crop_prediction_model.tflite')
with open(tflite_path, 'wb') as f:
    f.write(tflite_model)

print(f"💾 TinyML Model saved to: {tflite_path}")
print("🎉 Unit I (TinyML) Objectives Completed!")