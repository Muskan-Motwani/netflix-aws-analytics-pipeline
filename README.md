# 🎬 Netflix Analytics Pipeline — AWS + Python

An end-to-end data analytics project that takes the raw Netflix Movies and TV Shows dataset through a full cloud pipeline — cleaning, cloud storage, cataloging, SQL querying, and an interactive dashboard.

```
Netflix Dataset → Python (Cleaning & EDA) → Amazon S3 → AWS Glue → Amazon Athena (SQL) → Streamlit Dashboard
```

---

## 📌 Business Problem

Netflix's content catalog spans thousands of titles across countries, genres, and years. As a Data Analyst, the goal of this project was to simulate a real-world scenario: take messy raw data, build a cloud-based analytics pipeline around it, and surface insights that could inform a content strategy team about catalog composition, growth trends, and audience targeting.

## 🎯 Objectives

- Clean and prepare a real-world, messy dataset for analysis
- Store and catalog the data using cloud infrastructure (AWS)
- Query the data using SQL in a serverless environment (Athena)
- Build an interactive dashboard for business stakeholders to explore the data themselves

---

## 🏗️ Architecture

```
┌─────────────────────┐
│   Netflix Dataset    │   (Kaggle CSV)
└──────────┬───────────┘
           ▼
┌─────────────────────┐
│   Python Cleaning     │   pandas — nulls, duplicates, dtypes, feature engineering
│   & EDA (Jupyter)      │
└──────────┬───────────┘
           ▼
┌─────────────────────┐
│     Amazon S3          │   raw/ and processed/ buckets
└──────────┬───────────┘
           ▼
┌─────────────────────┐
│    AWS Glue Crawler    │   Auto-detects schema, builds Data Catalog
└──────────┬───────────┘
           ▼
┌─────────────────────┐
│    Amazon Athena       │   Serverless SQL queries on S3 data
└──────────┬───────────┘
           ▼
┌─────────────────────┐
│  Streamlit Dashboard   │   Interactive filters, KPIs, charts
└─────────────────────┘
```

*(See `architecture.png` for the visual diagram — add your exported version here.)*

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Data Cleaning & EDA | Python, Pandas, NumPy |
| Visualization (EDA) | Matplotlib, Seaborn |
| Cloud Storage | Amazon S3 |
| Data Cataloging | AWS Glue |
| SQL Querying | Amazon Athena |
| Dashboard | Streamlit, Plotly |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```
netflix-aws-analytics-pipeline/
├── notebooks/
│   └── Netflix_Analysis.ipynb      # Data cleaning + EDA
├── data/
│   ├── netflix_titles.csv          # Raw dataset
│   └── netflix_cleaned.csv         # Cleaned, analysis-ready dataset
├── sql/
│   └── queries.sql                 # Athena SQL queries
├── charts/
│   └── (EDA chart images)
├── screenshots/
│   └── (Dashboard screenshot)
├── app.py                          # Streamlit dashboard
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ How to Run This Project

### 1. Clone the repository
```bash
git clone https://github.com/Muskan-Motwani/netflix-aws-analytics-pipeline.git
cd netflix-aws-analytics-pipeline
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Jupyter notebook (optional — regenerates cleaned data & EDA charts)
```bash
jupyter notebook notebooks/Netflix_Analysis.ipynb
```

### 4. Run the Streamlit dashboard
```bash
streamlit run app.py
```
The dashboard will open automatically at `http://localhost:8501`.

---

## ☁️ AWS Pipeline Setup

1. **S3**: Created a bucket with `raw/` and `processed/` folders to store the original and cleaned datasets.
2. **Glue**: Ran a crawler on the `processed/` folder to auto-detect the schema and build a Data Catalog table.
3. **Athena**: Queried the cataloged table directly using SQL — no database server required. See [`sql/queries.sql`](sql/queries.sql) for all queries used.

---

## 📊 Key Insights

*(Fill this in with what you found — a few examples below to guide the format)*

- The United States, India, and the United Kingdom contribute the largest share of Netflix titles.
- Content additions to the catalog peaked between 2018–2020.
- TV-MA is the most common content rating, suggesting the catalog skews toward mature audiences.
- Movies significantly outnumber TV Shows in the overall catalog.
- International Movies and Dramas are the most common genres.

## 💡 Recommendations

*(Business-style recommendations based on the insights above)*

- Content acquisition teams could explore underrepresented countries/genres to diversify the catalog.
- Given the dominance of TV-MA content, consider expanding family-friendly (PG/TV-PG) titles to grow the younger audience segment.

---


## Dashboard Overview
![Dashboard Overview](screenshots/Screenshot%202026-07-09%20163613.png)

## Content by Country & Genre
![Top Countries and Genres](screenshots/Screenshot%202026-07-09%20163628.png)

## Content Growth Over Time
![Content Growth](screenshots/Screenshot%202026-07-09%20163640.png)

## Rating Distribution
![Rating Distribution](screenshots/Screenshot%202026-07-09%20163652.png)
```

---

## 🚀 Future Improvements

- Deploy the Streamlit app to Streamlit Community Cloud for a live, shareable link
- Add a recommendation-style feature (e.g. "similar titles") using content-based filtering
- Automate the S3 → Glue → Athena refresh with a scheduled AWS Lambda function

---

## 👩‍💻 Author

**Muskan Motwani**
Final-year BCA (Data Science) student | Data Analytics & ML enthusiast
[LinkedIn](#) • [GitHub](https://github.com/Muskan-Motwani)
