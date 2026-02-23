import pandas as pd
from detections import category_distribution, correlations_values, missing_values, outliers, trend_values


# Grouping all insights
def generate_all_insights(df):
    insights = []

    insights += category_distribution.detect_category_distribution(df)
    insights += correlations_values.detect_correlation(df)
    insights += missing_values.detect_missing_values(df)
    insights += trend_values.detect_trends(df)
    insights += outliers.detect_outliers(df)

    return insights








