# Smart Agriculture Analytics - Unit II (R Language)
# Upgraded script for Advanced Data Visualization

if (!require("ggplot2")) install.packages("ggplot2", repos = "http://cran.us.r-project.org")
if (!require("dplyr")) install.packages("dplyr", repos = "http://cran.us.r-project.org")

library(ggplot2)
library(dplyr)

# 1. Load Data
args <- commandArgs(trailingOnly = TRUE)
file_path <- if (length(args) > 0) args[1] else "../data/sensor_data.csv"

cat("Loading Data from:", file_path, "\n")
data <- read.csv(file_path)

# Ensure Crop_Status is treated as a Category (Factor) for graphing
data$Crop_Status <- as.factor(data$Crop_Status)

# 2. Generate Crop Health Report
report <- data %>%
  group_by(Crop_Status) %>%
  summarise(
    Avg_Moisture = mean(Soil_Moisture),
    Avg_Temp = mean(Temperature),
    Avg_Humidity = mean(Humidity),
    Avg_pH = mean(pH_Level),
    Total_Count = n()
  )

write.csv(report, "../reports/crop_health_summary.csv", row.names = FALSE)
cat("Saved Summary Report to reports folder.\n")

# ==========================================
# 3. ADVANCED VISUALIZATIONS (3 GRAPHS)
# ==========================================

# Graph 1: Scatter Plot (Temperature vs Soil Moisture)
p1 <- ggplot(data, aes(x=Temperature, y=Soil_Moisture, color=Crop_Status)) +
  geom_point(alpha=0.6, size=2) +
  scale_color_manual(values=c("0"="red", "1"="forestgreen"), labels=c("Needs Attention", "Healthy")) +
  labs(title="Graph 1: Environmental Impact on Crop Health",
       subtitle="Correlation between Temperature and Soil Moisture",
       x="Temperature (C)", y="Soil Moisture (%)", color="Crop Status") +
  theme_minimal()

ggsave("../reports/Graph1_Temp_vs_Moisture.png", plot=p1, width=7, height=5)
cat("Generated Graph 1: Scatter Plot\n")


# Graph 2: Boxplot (Humidity Distribution by Status)
p2 <- ggplot(data, aes(x=Crop_Status, y=Humidity, fill=Crop_Status)) +
  geom_boxplot(alpha=0.7) +
  scale_fill_manual(values=c("0"="orange", "1"="steelblue"), labels=c("Needs Attention", "Healthy")) +
  labs(title="Graph 2: Humidity Variance Assessment",
       subtitle="Statistical spread of humidity across crop conditions",
       x="Crop Status (0=Bad, 1=Good)", y="Humidity Level (%)") +
  theme_light() +
  theme(legend.position="none") # Hide legend as X-axis explains it

ggsave("../reports/Graph2_Humidity_Boxplot.png", plot=p2, width=7, height=5)
cat("Generated Graph 2: Boxplot\n")


# Graph 3: Density Plot (Soil pH Levels)
p3 <- ggplot(data, aes(x=pH_Level, fill=Crop_Status)) +
  geom_density(alpha=0.5) +
  scale_fill_manual(values=c("0"="red", "1"="green"), labels=c("Needs Attention", "Healthy")) +
  labs(title="Graph 3: Soil pH Distribution",
       subtitle="Density curve of pH levels colored by health status",
       x="Soil pH Level", y="Density") +
  theme_classic()

ggsave("../reports/Graph3_pH_Density.png", plot=p3, width=7, height=5)
cat("Generated Graph 3: Density Plot\n")

cat("Unit II (R Analysis) Completed Successfully with 3 Graphs.\n")