import os

# ==========================================
# WINDOWS & JAVA FIX FOR SPARK
# ==========================================
# This bypasses the Java Security Manager error and disables Hadoop cluster checks
os.environ["JAVA_TOOL_OPTIONS"] = "-Djava.security.manager=allow"
os.environ["HADOOP_USER_NAME"] = "admin"

import pandas as pd
import numpy as np
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, when, count

# Setup Paths
base_dir = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(base_dir, 'data')
big_data_path = os.path.join(data_dir, 'historical_climate_data.csv')
report_dir = os.path.join(base_dir, 'reports')

# Create reports folder if it doesn't exist
if not os.path.exists(report_dir):
    os.makedirs(report_dir)


# ==========================================
# PART A: SIMULATE THE BIG DATA "DATA LAKE"
# ==========================================
def generate_big_data(rows=100000):
    print(f"🌍 Simulating Big Data: Generating {rows} rows of historical climate data...")
    np.random.seed(42)

    regions = np.random.choice(['North_Field', 'South_Field', 'East_Field', 'West_Field', 'Greenhouse'], rows)
    moisture = np.random.uniform(5, 95, rows)
    temperature = np.random.uniform(10, 50, rows)

    df = pd.DataFrame({'Region': regions, 'Soil_Moisture': moisture, 'Temperature': temperature})
    df.to_csv(big_data_path, index=False)
    print(f"✅ Big Data file saved at: {big_data_path} ({os.path.getsize(big_data_path) / (1024 * 1024):.2f} MB)")


# ==========================================
# PART B: APACHE SPARK PROCESSING (UNIT IV)
# ==========================================
def run_spark_analytics():
    print("\n🚀 Starting Apache Spark Engine...")

    # Initialize Spark Session with Windows-safe configurations
    # We use a local warehouse directory to prevent HDFS crashes
    warehouse_path = "file:///" + os.path.join(base_dir, "spark-warehouse").replace('\\', '/')

    spark = SparkSession.builder \
        .appName("SmartAgri_BigData_Analytics") \
        .master("local[*]") \
        .config("spark.sql.warehouse.dir", warehouse_path) \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")  # This hides all those scary red warnings!

    print("📂 Loading data into Spark Distributed Memory...")
    spark_df = spark.read.csv(big_data_path, header=True, inferSchema=True)

    print("⚙️ Processing Data across simulated cluster...")
    processed_df = spark_df.withColumn(
        "Extreme_Weather",
        when((col("Temperature") > 40) & (col("Soil_Moisture") < 20), "Yes").otherwise("No")
    )

    summary_df = processed_df.groupBy("Region").agg(
        avg("Temperature").alias("Avg_Temp"),
        avg("Soil_Moisture").alias("Avg_Moisture"),
        count(when(col("Extreme_Weather") == "Yes", True)).alias("Total_Extreme_Alerts")
    ).orderBy(col("Total_Extreme_Alerts").desc())

    print("\n📊 SPARK ANALYTICS RESULT (Farm Region Risk Analysis):")
    summary_df.show()

    # Save the report
    final_report = summary_df.toPandas()
    report_path = os.path.join(report_dir, 'spark_region_analysis.csv')
    final_report.to_csv(report_path, index=False)

    print(f"💾 Spark Summary Report saved to: {report_path}")

    spark.stop()
    print("🛑 Spark Engine shutdown successfully. Unit IV Complete!")


if __name__ == "__main__":
    if not os.path.exists(big_data_path):
        generate_big_data(100000)
    run_spark_analytics()