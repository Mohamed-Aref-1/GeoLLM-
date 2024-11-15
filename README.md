# Earthquake Data Retrieval Using LLM

## Overview
This project enables users to query an earthquake database using natural language. It utilizes Google's Gemini language model to convert user queries into SQL commands, which are then executed on a local SQLite database containing earthquake records. The results are displayed through an interactive Streamlit web application.

## Project Components

### Natural Language to SQL Conversion

- **Google Gemini LLM**:
  - Converts natural language queries into SQL commands.
  - Example: "What is the magnitude of the earthquake at latitude 35.5 and longitude -120.3?"  
    becomes: `SELECT MAG FROM EARTHQUAKES WHERE LAT = "35.5" AND LONG = "-120.3";`

### SQLite Database

- **Database Structure**:
  - Table Name: `EARTHQUAKES`
  - Columns:  
    - `LAT` (Latitude)  
    - `LONG` (Longitude)  
    - `TYPE` (Type of earthquake)  
    - `MAG` (Magnitude of earthquake)

- **`Sql.py`**:
  - Creates the SQLite database and populates it with data from a CSV file.
  - Example CSV columns: `Latitude`, `Longitude`, `Type`, `Magnitude`.

### Streamlit Application

- **`main.py`**:
  - Accepts user input as a natural language question.
  - Generates an SQL query using the Gemini model.
  - Executes the query on the SQLite database.
  - Displays the result interactively in the web app.

## Installation

### Clone the Repository
```bash
git clone https://github.com/your-username/earthquake-data-retrieval.git
cd earthquake-data-retrieval
```
### Install Dependencies
```bash
pip install -r requirements.txt 
```

### Set Up the Environment Variables
Create a .env file in the root directory of the project and add your Google API key:

```bash
GOOGLE_API_KEY=your_google_api_key
```
### Prepare the SQLite Database
Ensure you have your earthquake data as a CSV file (e.g., database.csv).
Run Sql.py to create the SQLite database (earthquake.db) and populate it with data from the CSV file:

```bash
python Sql.py
```

Project Structure
`main.py`: Streamlit app to interface with the Google Gemini model, convert natural language queries to SQL, and display results.
`Sql.py`: Script to set up the SQLite database by creating a table and inserting records from a CSV file.
`requirements.txt`: List of dependencies required to run the project.

### Usage
### Run the Streamlit App
```bash
streamlit run main.py
```

### Enter a Query
### Enter your query in the input box. For example:

```bash
What is the magnitude of the earthquake at latitude 35.5 and longitude -120.3?
```

### View Results
The application will display the generated SQL query and retrieve the corresponding data from the SQLite database.

### Example Query
If the user enters:

```bash
What is the magnitude of the earthquake at latitude 35.5 and longitude -120.3?
```
The Gemini model will convert this to:

```bash
SELECT MAG FROM EARTHQUAKES WHERE LAT = "35.5" AND LONG = "-120.3";
```

### Files
`main.py`: Contains the Streamlit application code.
`Sql.py`: Creates the SQLite database and populates it with earthquake data.
`requirements.txt`: Lists required libraries and dependencies for the project.
`.env`: Contains your API key (not included in the repo for security).
### Requirements
The dependencies required to run this project are:

`streamlit`
`google-generativeai`
`python-dotenv`
`langchain`
`PyPDF2`
`chromadb`
`faiss-cpu`
`pdf2image`

### To install all dependencies, run:

```bash
pip install -r requirements.txt
```





