# Importing Libraries
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

#Connecting to the Database
host = "localhost"
port = '3306'
database = "text_to_sql"
username = "root"
password = "pass123"
mysqluri = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

db = SQLDatabase.from_uri(mysqluri,sample_rows_in_table_info=1)

# Create the LLM Prompt Template

template = """Based on the table schema below, write a SQL query that would answer the user's question. 
Remember : Only write the SQL query and nothing else. Do not include any explanations or comments. Provide me SQL query in single line without any line breaks.
Table Schema: {table_info}
Question: {question}
SQL Query:
"""
promt = ChatPromptTemplate.from_template(template)

#get the schema of the database
def get_schema(db_schema):
    return db_schema.get_table_info()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                            api_key="API Key")#Replace with your API key)

#Create the sql query chain using the LLM and the prompt template 

sql_chain = (RunnablePassthrough.assign(table_info = lambda _:get_schema(db)) 
            | promt 
            | llm.bind(stop=["\nSQLResult:"]) 
            | StrOutputParser()) 

#Create the UI using Streamlit
st.set_page_config(page_title="Text to SQL Query Generator", page_icon=":guardsman:", layout="centered")
st.title("Text to SQL Query Generator")
st.subheader("Ask a question about the database and get the corresponding SQL query")
user_question = st.text_input("Enter your question here")

if st.button("Generate SQL Query"):
     if user_question:
        with st.spinner("Generating SQL Query..."):
            response = sql_chain.invoke({"question":user_question})
            st.code(response, language="sql")
     else:
        st.warning("Please enter a question to generate the SQL query.")
