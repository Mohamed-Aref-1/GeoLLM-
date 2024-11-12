from dotenv import load_dotenv
import os
import streamlit as st
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure GenAI Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("GOOGLE_API_KEY not found. Please set it in the .env file.")
else:
    genai.configure(api_key=api_key)

# Function to load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database is named EARTHQUAKES and has the following columns: LAT (latitude), 
    LONG (longitude), TYPE, and MAG (magnitude).
    
    For example:
    - Question: "What is the magnitude of the earthquake at latitude 35.5 and longitude -120.3?" 
      SQL command: SELECT MAG FROM EARTHQUAKES WHERE LAT = "35.5" AND LONG = "-120.3";
      
    Make sure not to include `sql` or ``` in your response.
    """
]

# Streamlit App
st.set_page_config(page_title="Retrieve Earthquake Data")
st.header("Earthquake Data Retrieval Using LLM")

question = st.text_input("Enter your question (e.g., What is the magnitude of the earthquake at latitude 35.5 and longitude -120.3?)", key="input")
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    if not api_key:
        st.error("API Key not set. Check the .env file.")
    else:
        response = get_gemini_response(question, prompt)
        st.write("Generated SQL Query:", response)
        
        try:
            result = read_sql_query(response, "earthquake.db")
            st.subheader("The Response is")
            for row in result:
                st.write(row)
        except Exception as e:
            st.error(f"Error executing query: {e}")

print(os.getenv("GOOGLE_API_KEY"))  
