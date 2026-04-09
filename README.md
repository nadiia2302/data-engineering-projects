# Book Data Ingestion & Transformation (Task #1)
This project demonstrates a data engineering pipeline that processes a "corrupted" JSON file, ingests the cleaned data into a relational database (SQLite), and performs analytical transformations directly within the database using SQL.

## 🚀 Overview
The solution covers the following requirements:

Data Cleaning & Parsing: The source file task1_d.json was not a valid JSON format. I implemented a script to clean the raw string data and convert it into a valid list of Python dictionaries.

Database Ingestion: Data is uploaded into a SQLite database. The id field is stored as TEXT to handle long integers and prevent overflow errors.

In-Database Transformation: The final summary table is built using a single SQL query to ensure all business logic resides within the RDBMS.

Currency Conversion: EUR prices are converted to USD using the rate €1 = $1.2.

Aggregation: Books are grouped by their publication year to calculate counts and averages.

Precision: Average prices are rounded to 2 decimal places (cents).

## 📁 Project Structure
task_1.py: Contains the logic for reading, cleaning, and preparing the raw JSON data.

database.py: Handles the SQLite connection, table creation, data insertion, and the execution of the transformation query.

task1_d.json: The raw source data file.

books.db: The generated SQLite database file.

## 🛠️ How to Run
Clone the repository.

Ensure task1_d.json is in the root directory.

Execute the database script:

Bash
python database.py
# 📊 Summary Table Schema
The resulting summary_transformation table includes:
- year: The year of publication.
- count_book: Total number of books published that year.
- average_currency: The average price in USD for that year, rounded to two decimal places.
- count_book: Total number of books published that year.

average_currency: The average price in USD for that year, rounded to two decimal places.
