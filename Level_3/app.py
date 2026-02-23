import streamlit as st
import pandas as pd
from total_insights import generate_all_insights
import google.generativeai as genai
from prompt import build_prompt
import plotly.express as px

st.set_page_config(page_title="AI Data Analyzer", layout="wide")


st.title("📊AI Data Analyzer")

# API Configuration
genai.configure(api_key="API_KEY")
model = genai.GenerativeModel("MODEL_NAME")

# File upload
uploaded_file = st.file_uploader("Upload CSV or Excel File", type=["csv", "xlsx"])

if uploaded_file is not None:

    if "df" not in st.session_state:
        if uploaded_file.name.endswith(".csv"):
            st.session_state.df = pd.read_csv(uploaded_file)
        else:
            st.session_state.df = pd.read_excel(uploaded_file)
    
    DF = st.session_state.df
    st.dataframe(DF)

    
    numeric_col = DF.select_dtypes('number').columns
    categorical_col = DF.select_dtypes('object').columns

    if len(categorical_col) > 0:
        # Pie Chart
        pie_category = st.selectbox("Select Category for Pie Chart", categorical_col)
        pie_value = st.selectbox("Select Value for Pie Chart", numeric_col)

        grouped = DF.groupby(pie_category)[pie_value].sum().reset_index()

        fig_p = px.pie(
            grouped,
            names = pie_category,
            values = pie_value,
            title = f"{pie_value} Distribution by {pie_category}"
            )
        st.plotly_chart(fig_p)

        # Plots
        x_axis = st.selectbox("Select X-axis", DF.columns)
        y_axis = st.selectbox("Select Y-axis", numeric_col)

        chart_type = st.selectbox("Select Chart Type", ["Line", "Bar", "Scatter"])

        if chart_type == "Line":
            fig = px.line(DF, x=x_axis, y=y_axis)
        elif chart_type == "Bar":
            fig = px.bar(DF, x=x_axis, y=y_axis)
        elif chart_type == "Scatter":
            fig = px.scatter(DF, x=x_axis, y=y_axis)
        
        st.plotly_chart(fig)

    # Generating Insights only once
    if "insights" not in st.session_state:
        with st.spinner("Generating AI Insights..."):
            insights = generate_all_insights(DF)

            query = build_prompt(DF)
            response = model.generate_content(
                f'{query}'
            )


            st.session_state.insights = response.text

    st.subheader("📌Initial AI Insights")
    st.write(st.session_state.insights)

    # CHAT SYSTEM

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Ask me anything about the uploaded dataset!"
            }
        ]
    
    if "model_response_cache" not in st.session_state:
        st.session_state.model_response_cache = {}

    user_query = st.chat_input("Ask your question")

    if user_query:
        st.session_state.messages.append({"role":"user", "content": user_query})

        # check if answer already exists
        if user_query in st.session_state.model_response_cache:
            cached_response = st.session_state.model_response_cache[user_query]

            st.session_state.messages.append({
                "role": "assistant",
                "content" : cached_response
            })
        else:
            with st.spinner("Analyzing your data..."):
                contextual_prompt =f"""
                Your are a AI Data Analyst.
                here is my {DF.to_string()} dataframe.
                Some inisghts are {st.session_state.insights}.

                User question:
                {user_query}
                
                ANSWER USER QUERIES ONLY BASED ON THE PROVIDED DATASET.
                IF THE ANSWER CANNOT BE DETERMINED FROM THE DATASET, SAY SO.
                """

                re = model.generate_content(contextual_prompt)
                st.session_state.messages.append({"role": "assistant", "content":re.text})
        
        # Display chat history
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

else:
    st.write("Pleaase upload a XLSV and CSV file to begin.")
        

