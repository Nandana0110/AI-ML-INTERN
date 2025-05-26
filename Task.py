import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Step 2: Load Dataset
df = pd.read_csv(r"c:\Users\AL SharQ\Downloads\intern\Titanic-Dataset.csv")  

# Step 3: Explore the Data
print(df.head())
print(df.info())
print(df.describe())

#Step 2: Handle missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)

# Step 5: Convert Categorical Columns
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)


# Step 6: Normalize Numerical Features
scaler = MinMaxScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Step 7: Visualize Outliers
sns.boxplot(x=df['Age'])
plt.title("Boxplot - Age")
plt.show()

sns.boxplot(x=df['Fare'])
plt.title("Boxplot - Fare")
plt.show()

# Step 8: Remove Outliers (IQR Method)
for col in ['Age', 'Fare']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]

# Final Output
print("Cleaned Data Preview:")
print(df.head())
