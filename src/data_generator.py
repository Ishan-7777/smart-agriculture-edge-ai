import pandas as pd
import numpy as np
import os

# Ensure the 'data' folder exists
# We go up one level (..) to find the project root, then into 'data'
output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def generate_sensor_data(n_samples=2000):
    print("🌱 Starting Sensor Simulation...")

    # 1. Simulate Soil Moisture (10% to 90%)
    np.random.seed(42)  # Consistent data
    soil_moisture = np.random.uniform(10, 90, n_samples)

    # 2. Simulate Temperature (15°C to 45°C)
    temperature = np.random.uniform(15, 45, n_samples)

    # 3. Simulate Humidity (30% to 90%)
    humidity = np.random.uniform(30, 90, n_samples)

    # 4. Simulate pH Level (4.5 to 8.0)
    ph_level = np.random.uniform(4.5, 8.0, n_samples)

    # Create a DataFrame
    df = pd.DataFrame({
        'Soil_Moisture': soil_moisture,
        'Temperature': temperature,
        'Humidity': humidity,
        'pH_Level': ph_level
    })

    # 5. Define Logic for "Crop Status" (Simulating an Expert/Labeling)
    # Logic: If Moisture < 30 OR Temp > 40 -> Needs Attention (0), Else Healthy (1)
    conditions = [
        (df['Soil_Moisture'] < 30) | (df['Temperature'] > 40),
        (df['Soil_Moisture'] >= 30) & (df['Temperature'] <= 40)
    ]
    choices = [0, 1]  # 0 = Needs Attention, 1 = Healthy

    df['Crop_Status'] = np.select(conditions, choices, default=0)

    # 6. Save to CSV
    output_path = os.path.join(output_dir, 'sensor_data.csv')
    df.to_csv(output_path, index=False)

    print(f"✅ Simulation Complete!")
    print(f"📊 Generated {n_samples} rows of synthetic sensor data.")
    print(f"💾 Data saved to: {os.path.abspath(output_path)}")
    print("\nPreview:")
    print(df.head())


if __name__ == "__main__":
    generate_sensor_data()