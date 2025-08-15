# csv-to-sqlite

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

Convert any customer-facing CSV file into a clean SQLite database using Python.  
Useful for SaaS onboarding, data migrations, and internal analytics tooling.

---

## 🧠 Why I Built This

Customer CSVs are often messy — headers, whitespace, missing values.  
This tool converts them into clean, queryable SQLite databases with zero setup.

---

## ⚙️ Features

- Clean column names and drop null rows
- Convert to SQLite with schema inference
- Save as `.db` file for analysis or ingestion
- Lightweight – no ORM or extra dependencies

---

## 🖥️ CLI Usage

```bash
python convert_to_sqlite.py sample.csv output.db
📦 Installation
bash
Copy
Edit
git clone https://github.com/andreadeyemi/csv-to-sqlite.git
cd csv-to-sqlite
python3 convert_to_sqlite.py sample.csv output.db
🔍 Use Cases
Internal dashboards and queries

Prepping data for BI tools

Quick data exploration

SaaS onboarding automation

🧱 Built With
Python 3.8+

sqlite3

Standard libraries only

