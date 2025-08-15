# csv-to-sqlite

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

> A lightweight command-line tool to convert messy customer CSVs into clean, queryable SQLite databases using Python.  
> Perfect for SaaS onboarding, internal analytics, BI pipelines, and fast data ingestion.

---

## 🚀 Why I Built This

In SaaS and ops roles, you're often handed chaotic CSVs — inconsistent headers, null rows, bad whitespace.  
This utility cleans them up and instantly converts them into `.db` files for fast queries or downstream tools — no config, no ORM, no headaches.

---

## ⚙️ Features

- 📦 One-command conversion from `.csv` to `.db`
- 🧹 Cleans headers, drops null rows, trims whitespace
- 🧠 Auto-infers schema using SQLite engine
- 🔎 Ideal for data ingestion, pre-BI prep, and debugging pipelines
- 🪶 No heavy dependencies — uses standard libraries + `sqlite3`

---

## 💻 CLI Usage

```bash
python convert_to_sqlite.py sample.csv output.db
📦 Install & Run
bash
Copy
Edit
# Clone the repo
git clone https://github.com/andreadeyemi/csv-to-sqlite.git
cd csv-to-sqlite

# Run the script with any .csv file
python3 convert_to_sqlite.py sample.csv output.db
🧠 Use Cases
SaaS customer onboarding automations

Data migration QA

Internal dashboards & queries

Quick smoke tests for data pipelines

BI pre-processing (Metabase, Tableau, Looker)

## 🖼️ Output Preview

Below is a snapshot of the resulting SQLite table from the sample CSV:

![Output Screenshot](https://raw.githubusercontent.com/andreadeyemi/csv-to-sqlite/main/output_preview.png)



🛠 Built With
Python 3.8+

sqlite3

Zero external dependencies

📁 File Structure
arduino
Copy
Edit
├── convert_to_sqlite.py     # main script
├── sample.csv               # input sample data
├── output_preview.png       # visual SQLite result
├── README.md
├── LICENSE
├── requirements.txt
🧱 About the Author
André Adeyemi
Customer Success & SaaS Engineering | Python • APIs • BI • Automation
🔗 LinkedIn | (https://linkedin.com/in/andre-adeyemi)

🪪 License
MIT – free to use, adapt, and share.
