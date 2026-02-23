import pandas as pd

def detect_correlation(df):
    insights = []

    numeric_df = df.select_dtypes(include='number')
    corr_matrix = numeric_df.corr()

    for col1 in corr_matrix.columns:
        for col2 in corr_matrix.columns:
            if col1 != col2:
                corr_value = corr_matrix.loc[col1, col2]

                if abs(corr_value) > 0.7:
                    insights.append({
                        "type": "correlation",
                        "variables": (col1, col2),
                        "value": corr_value
                    })
    return insights