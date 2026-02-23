import pandas as pd 

def detect_missing_values(df):
    insights = []

    for col in df.columns:
        missing_percent = df[col].isnull().mean()*100

        if missing_percent > 10:
            insights.append({
                "type": "warning",
                "message": f"{col} has {missing_percent:.2f}% missing values"
            })

    return insights