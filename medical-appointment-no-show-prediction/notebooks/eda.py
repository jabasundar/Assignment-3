import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("medical-appointment-no-show-prediction/data/processed/processed_medical_data.csv")

print(df.shape)
df.head()

sns.countplot(x="no_show", data=df)
plt.title("No Show Distribution (0 = Showed, 1 = No Show)")
plt.show()

sns.barplot(x="age_group", y="no_show", data=df)
plt.title("No Show Rate by Age Group")
plt.xticks(rotation=30)
plt.show()

sns.boxplot(x="no_show", y="health_risk_score", data=df)
plt.title("Health Risk vs No Show")
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()