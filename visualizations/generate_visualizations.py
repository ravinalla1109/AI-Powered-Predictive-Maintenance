import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("../data/processed_data.csv")

# Example visualization: Feature correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.savefig("../visualizations/feature_correlation_heatmap.png")
plt.close()

# Example visualization: Distribution of target variable
plt.figure(figsize=(8, 6))
sns.countplot(x="failure", data=data)
plt.title("Failure Distribution")
plt.savefig("../visualizations/failure_distribution.png")
plt.close()

print("Visualizations saved successfully!")
