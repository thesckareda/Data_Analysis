import pandas as pd

def detect_trends(df):
    insights = []

    date_cols = df.select_dtypes(include='datetime').columns

    if len(date_cols) == 0:
        return insights 
    
    numeric_cols = df.select_dtypes(include='number').columns 

    if len(numeric_cols) == 0:
        return insights
    
    date_col = date_cols[0]
    num_col = numeric_cols[0]

    monthly = df.groupby(df[date_col].dt.to_period("M"))[num_col].sum()
    growth = monthly.pct_change().mean()

    if growth > 0:
        trend = "upward"
    else:
        trend = "downward"

    insights.append({
        "type": "trend",
        "column": num_col,
        "direction": trend
    })

    return insights