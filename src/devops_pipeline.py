import subprocess
import time
import os
import shutil
import sys

# Setup paths
base_dir = os.path.dirname(os.path.dirname(__file__))
src_dir = os.path.join(base_dir, 'src')
models_dir = os.path.join(base_dir, 'models')
prod_dir = os.path.join(base_dir, 'production_deploy')

print("🚀 STARTING SMART AGRI CI/CD DEVOPS PIPELINE...")
print("=====================================================")


def run_step(step_name, script_name):
    print(f"⏳ [{step_name}] Starting...")
    time.sleep(1)  # Small delay to simulate cloud loading
    script_path = os.path.join(src_dir, script_name)

    # Run the script using UTF-8 encoding so it understands our emojis!
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=True,
        text=True,
        encoding='utf-8'  # <--- THIS IS THE MAGIC FIX
    )

    if result.returncode == 0:
        print(f"✅ [{step_name}] SUCCESS")
    else:
        print(f"❌ [{step_name}] FAILED! Pipeline Stopped.")
        print(result.stderr)
        exit(1)


# Step 1: Automated Data Build (Unit I)
run_step("STAGE 1: Automated Sensor Data Simulation", "data_generator.py")

# Step 2: Automated AI Training & Testing (Unit I)
run_step("STAGE 2: TinyML Edge AI Training & Conversion", "train_model.py")

# Step 3: Automated Analytics (Unit II)
run_step("STAGE 3: R Analytics & Report Generation", "run_r_analysis.py")

# Step 4: Automated Big Data Processing (Unit IV)
run_step("STAGE 4: Apache Spark Distributed Processing", "big_data_spark.py")

# Step 5: Continuous Deployment (CD)
print("\n⏳ [STAGE 5: Production Deployment] Starting...")
time.sleep(1)

if not os.path.exists(prod_dir):
    os.makedirs(prod_dir)

source_model = os.path.join(models_dir, 'crop_prediction_model.tflite')
dest_model = os.path.join(prod_dir, 'crop_prediction_model_PROD.tflite')

if os.path.exists(source_model):
    shutil.copy(source_model, dest_model)
    print(f"✅[STAGE 5: Production Deployment] SUCCESS!")
    print(f"📦 Model securely deployed to: {dest_model}")
else:
    print("❌ [STAGE 5: Production Deployment] FAILED - Model not found!")
    exit(1)

print("\n=====================================================")
print("🎉 DEVOPS PIPELINE COMPLETED SUCCESSFULLY!")
print("All systems are tested, built, and deployed without human intervention.")