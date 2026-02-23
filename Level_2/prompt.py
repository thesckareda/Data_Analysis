### This function generates the prompt as per the query.

def build_prompt(df, question):
    columns = ", ".join(df.columns)

    prompt = f'''
    You are a data analyst.
    The dataset has the following columns:
    {columns} 

    Write ONLY pandas code (no explaination).
    DO NOT use quotes.
    The dataframe name is df.

    Question: 
    {question}
    '''
    return prompt