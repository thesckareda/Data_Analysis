import pandas as pd

def detect_category_distribution(df):
    insights = []

    categorical_col = df.select_dtypes(include='object').columns

    for col in categorical_col:
        distribution = df[col].value_counts(normalize=True)

        if distribution.iloc[0] > 0.5:
            insights.append({
                "type": "dominance",
                "column": col,
                "dominant value": distribution.index[0],
                "percentage": distribution.iloc[0]*100
            })

    return insights