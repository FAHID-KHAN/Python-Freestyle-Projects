"""
Data preprocessing is a critical step in data science tasks, ensuring that raw data is transformed into a clean, organized, and structured format suitable for analysis. A data preprocessing pipeline streamlines this complex process by automating a series of steps, enabling data professionals to efficiently and consistently preprocess diverse datasets. So, if you want to learn how to create a Data Preprocessing pipeline, this article is for you. In this article, I will take you through building a Data Preprocessing pipeline using Python.

What is a Data Preprocessing Pipeline?
Data Preprocessing involves transforming and manipulating raw data to improve its quality, consistency, and relevance for analysis. It encompasses several tasks, including handling missing values, standardizing variables, and removing outliers. By performing these preprocessing steps, data professionals ensure that subsequent analysis is based on reliable and accurate data, leading to better insights and predictions.

A data preprocessing pipeline is a systematic and automated approach that combines multiple preprocessing steps into a cohesive workflow. It serves as a roadmap for data professionals, guiding them through the transformations and calculations needed to cleanse and prepare data for analysis. The pipeline consists of interconnected steps, each of which is responsible for a specific preprocessing task, such as:

imputing missing values
scaling numeric features
finding and removing outliers
or encoding categorical variables
By following the predefined sequence of operations, the pipeline ensures consistency, reproducibility, and efficiency in overall preprocessing steps.
    """

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def data_preprocessing_pipeline(data):
    #Identify numeric and categorical features
    numeric_features = data.select_dtypes(include=['float', 'int']).columns
    categorical_features = data.select_dtypes(include=['object']).columns

    #Handle missing values in numeric features
    data[numeric_features] = data[numeric_features].fillna(data[numeric_features].mean())

    #Detect and handle outliers in numeric features using IQR
    for feature in numeric_features:
        Q1 = data[feature].quantile(0.25)
        Q3 = data[feature].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (1.5 * IQR)
        upper_bound = Q3 + (1.5 * IQR)
        data[feature] = np.where((data[feature] < lower_bound) | (data[feature] > upper_bound),
                                 data[feature].mean(), data[feature])

    #Normalize numeric features
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[numeric_features])
    data[numeric_features] = scaler.transform(data[numeric_features])

    #Handle missing values in categorical features
    data[categorical_features] = data[categorical_features].fillna(data[categorical_features].mode().iloc[0])

    return data


df = pd.read_csv("data.csv")

print("Original Data: ")
print(df)

cleaned_data = data_preprocessing_pipeline(df)
print("Preprocessed Data: ")
print(cleaned_data)
    