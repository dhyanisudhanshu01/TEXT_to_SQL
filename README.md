# 🧠 Text to SQL Query Generator

An interactive AI-powered web application that converts natural language questions into SQL queries using **Google Gemini** and **LangChain**, with a **Streamlit UI**.

This app connects to a MySQL database, understands the schema, and generates accurate SQL queries based on user input.

---

## 🚀 Features

- Natural Language → SQL conversion  
- Uses Gemini 2.5 Flash model  
- Automatic database schema understanding  
- Clean and interactive UI built with Streamlit  
- MySQL database integration  
- Single-line SQL output (no explanations)

---

## 🛠️ Tech Stack

- **LLM Framework:** [LangChain](https://www.langchain.com/)
- **LLM Provider:** [Google Gemini](https://ai.google.dev/)
- **UI Framework:** [Streamlit](https://streamlit.io/)
- **Database:** MySQL  
- **Driver:** PyMySQL  

---

## 🧠 How It Works

1. Connects to MySQL database using SQLAlchemy URI  
2. Fetches table schema dynamically  
3. Sends schema + user question to Gemini model  
4. Model generates SQL query  
5. Displays SQL query in the UI  

---

## 📂 Project Structure
Text_to_SQL/
├── data
    ├── csv files
├── src
    ├── app.py
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

git clone https://github.com/dhyanisudhanshu01/TEXT_to_SQL.git
cd TEXT_to_SQL

