# 🌾 Smart Agriculture Analytics Platform (IoT Digital Twin)

## 📌 Project Overview
This project is a **Software-Defined IoT Platform** simulating an end-to-end Smart Agriculture system. It demonstrates the complete data lifecycle: from Edge AI sensor simulation to Big Data cloud analytics, interactive data visualization, and automated DevOps deployment.

## 🚀 Technologies & Frameworks Used
* **Unit I (Edge AI/Hardware):** Wokwi IoT Simulator, TinyML (TensorFlow Lite), Python Data Generation
* **Unit II (Analytics & Automation):** R Language (`ggplot2`, `dplyr`), Python Subprocess Automation
* **Unit III (Business Intelligence):** Microsoft Power BI
* **Unit IV (Big Data Processing):** Apache Spark (`PySpark`)
* **Unit V (DevOps / MLOps):** GitHub Actions (CI/CD), Automated Local Deployment Pipeline

## 🏗️ System Architecture
1. **IoT Edge Simulation:** Generated synthetic sensor data (Soil Moisture, Temp, pH) and deployed a quantized `TinyML` neural network to simulate real-time edge predictions.
2. **Automated Data Processing:** Engineered a pipeline that triggers R scripts to clean data and generate statistical distributions (Scatter, Boxplots, Density).
3. **Interactive Dashboard:** Built a Power BI dashboard with dynamic filtering to provide farmers with real-time KPI gauges and crop health ratios.
4. **Distributed Big Data:** Utilized Apache Spark to process a massive historical climate dataset (100,000+ rows), grouping data across farm regions to detect extreme weather anomalies.
5. **CI/CD Pipeline:** Developed an automated DevOps orchestrator (`devops_pipeline.py`) and a GitHub Actions `.yml` workflow to automatically test, build, and deploy the AI model to production without human intervention.

## 👨‍💻 How to Run
Run the master DevOps pipeline to execute all stages automatically:
`python src/devops_pipeline.py`