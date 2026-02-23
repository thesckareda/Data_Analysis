import google.generativeai as genai
from prompt import build_prompt
from filter import safe_execute
import pandas as pd


# This dataset tracks the academic and professional performance of the top 52 universites in Japan(2026 Edition). 
df = pd.read_csv('data.csv')

genai.configure(api_key="API_KEY")
model = genai.GenerativeModel("MODEL_NAME")


print("------------------------------------------WELCOME TO DATA ANALYZER(LEVEL_02)------------------------------------------")
query = input("Enter a query: ")

prompt = build_prompt(df, query)

response = model.generate_content(
    f'{prompt}'
)

final_code = safe_execute(response.text)

try:
    # this will execute the code
    exec("print(" + final_code + ")")
    
except Exception as e:
    print(f"error: {e}")
    print("Make sure you have entered only one question.")

print("------------------------------------------END------------------------------------------")