# Data_analysis
# Level 3 – AI Dashboard + Conversational Data Analyst 

Objective: Building a complete interactive AI analytics tool.

Functionality:

📂 File Upload
Supports CSV and Excel files
Saves dataset in session state

📊 Interactive Visualizations
Pie chart for categorical distribution
Line, Bar, Scatter plots
User-defined axis selection

📌 Initial AI Insights
Automated insights using rule-based engine
AI-generated explanation using Gemini API

💬 Conversational AI Chat
Users can ask questions about their dataset
AI answers purely based on uploaded data
Uses session memory with st.session_state
Caches responses for repeated queries

🧠 Context-Aware Analysis
The AI takes in:
Full dataset context
Previously generated insights
User question and answers with responses that are grounded only in the uploaded data.

🏗 System Architecture
User Upload --> Data Cleaning & Processing --> Rule-Based Insight Engine --> LLM AI Insight Generation --> Interactive Dashboard --> Chat-Based AI Analyst

🛠 Tech Stack
- Python
- Streamlit
- Pandas
- Plotly
- LLM API

🎯 What Makes This Level 3?
This project is more than a dashboard.
It combines:
- Statistical analysis
- Pattern recognition
- Automated insight generation
- Natural language interaction
- Context-aware AI responses
- Interactive visualization

It models a basic AI analytics tool like:
- AI-infused BI tools
- Conversational analytics platforms
- Smart data assistants

📌 Example Use Cases
“Which category generates the most revenue?”
“Are there any significant correlations?”
“Why might profit be volatile?”
“Plot trends over time.”
“Are there any outliers in sales?”
