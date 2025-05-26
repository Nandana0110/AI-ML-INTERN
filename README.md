# AI-ML-INTERN
A project on data cleaning and preprocesing 

Titanic Dataset Preprocessing and Cleaning
This project focuses on preprocessing and cleaning the Titanic dataset in preparation for data analysis or machine learning modeling. The steps include data loading, exploration, handling missing values, encoding categorical variables, normalization, outlier visualization, and removal.
Steps Performed
Load Data: Reads the Titanic dataset from a CSV file.

Explore Data: Displays basic info and statistics.

Handle Missing Values:

Fill missing Age with median.

Fill Embarked with mode.

Drop the Cabin column.

Encode Categories: Converts Sex and Embarked to numeric using one-hot encoding.

Normalize Data: Scales Age and Fare to a 0–1 range.

Visualize Outliers: Uses boxplots to identify outliers.

Remove Outliers: Applies the IQR method on Age and Fare.

Final Output: Displays a preview of the cleaned data.
