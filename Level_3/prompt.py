from total_insights import generate_all_insights

def build_prompt(df):
    columns = ", ".join(df.columns)

    prompt = f"""
    You are a AI data analyst.
    The dataset has the following columns:
    {columns}

    These are some insights:
    {generate_all_insights(df)}

    Analyze the insights and categorize maoin insights properly to display in 
    my dashboard as a AI data analyst.

    
    """

    return prompt