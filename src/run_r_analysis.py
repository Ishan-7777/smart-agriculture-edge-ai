import subprocess
import os

# Define paths
base_dir = os.path.dirname(os.path.dirname(__file__))
r_script_path = os.path.join(base_dir, 'src', 'analytics.R')
data_path = os.path.join(base_dir, 'data', 'sensor_data.csv')
r_executable = "Rscript" # Assumes R is in your Windows PATH

print("🔄 Starting R Automation Pipeline (Unit II)...")

# Verify R is installed
try:
    subprocess.run([r_executable, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except FileNotFoundError:
    print("❌ Error: R is not installed or not in PATH.")
    print("👉 Please install R from https://cran.r-project.org/bin/windows/base/")
    exit(1)

# Run the R script
cmd = [r_executable, r_script_path, data_path]
result = subprocess.run(cmd, capture_output=True, text=True)

# Print Output
print(result.stdout)
if result.stderr:
    print("⚠️ R Warnings/Errors:")
    print(result.stderr)

print("🎉 R Automation Finished.")