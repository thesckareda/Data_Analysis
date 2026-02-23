import pandas as pd


# Detecting Outliers
def detect_outliers(df):
    insights = []

    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1 # Interquartile Range

        lower = Q1 - 1.5*IQR
        upper = Q3 + 1.5*IQR

        outliers = df[(df[col] < lower )| (df[col] > upper)]

        if len(outliers) > 0:
            insights.append({
                "type": "outlier",
                "column": col,
                "count": len(outliers)
            })
                      
    return insights
