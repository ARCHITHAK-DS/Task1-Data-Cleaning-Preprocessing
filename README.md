# 🎬 Netflix Movies and TV Shows — Data Cleaning & Preprocessing

## 📌 Project Overview

This project focuses on cleaning and preprocessing a raw Netflix dataset using **Microsoft Excel** and **Python (Pandas)**. The dataset contained inconsistent formatting, missing values, text issues, and columns requiring structural transformation before any analysis could be performed.

The objective was to transform raw, messy data into a **clean, structured, and analysis-ready dataset**.


## 📂 Repository Structure

netflix-data-cleaning/
│
├── Datasets                                         # Includes Uncleaned & Cleaned dataset
├── screenshots/                                     # output screenshots 
├── Python code for cleaning and preprocessing.py    # Full Python cleaning script
├── README.md                                        # Project documentation
└── requirements.txt                                 # Python dependencies
 ## Repository Structure

```text
netflix-data-cleaning/
│── Datasets/
│   ├── netflix1.csv
│   ├── netflix_cleaned.csv
│   └── netflix_cleaned.xlsx
│
│── screenshots/
│
│── cleaning_and_preprocessing.py
│── README.md
│── requirements.txt
```

## 📊 Dataset Information

| Property |             | Details |
|----------|             |---------|
| **Dataset** |          | Netflix Data |
| **Source** |           |[Kaggle — https://www.kaggle.com/datasets/ariyoomotade/netflix-data-cleaning-analysis-and-visualization/data |
| **Original Shape** |   | 8,790 rows × 10 columns |
| **Final Shape** |      |8,790 rows × 14 columns |


## 🛠️ Tools & Technologies

| Tool |              | Purpose |
|-----------------|   |--------------------------------------|
| Microsoft Excel |   |Initial exploration and manual cleaning |
| Python 3.x |        | Automated preprocessing pipeline |
| Pandas |            | Data manipulation and transformation |
| NumPy |             | Numerical operations |
| Regex (`re`) |      | Pattern-based text cleaning |


## 🧹 Data Cleaning & Preprocessing Steps

### 1. Handling Null Values
- Identified all missing values across every column.
- Replaced missing text fields with `"Unknown"`.
- Applied **forward fill** to populate remaining null rows contextually.

### 2. Removing Duplicate Records
- Detected and removed all duplicate rows to ensure data consistency and integrity.

### 3. Standardizing Column Names
- Converted all column names to **snake_case**:
  - Lowercased all characters
  - Removed special characters
  - Replaced spaces with underscores

Release Year  →  release_year
Date Added    →  date_added


### 4. Removing Extra Whitespace
- Stripped leading and trailing whitespace from all text-based columns.

### 5. Standardizing Text Values
- Enforced consistent capitalization across categorical columns such as `type`, `country`, and `director`.

movie    →  Movie
tv show  →  Tv Show

### 6. Cleaning and Formatting Dates
- Converted the `date_added` column to proper datetime format.
- Reformatted all date entries to `DD-MM-YYYY`.

9/25/2021  →  25-09-2021

### 7. Splitting the Duration Column
- Split the single `duration` column into two meaningful columns:
  - `duration_value` — the numeric part
  - `duration_unit` — the unit (min / seasons)

90 min      →  90   |  min
2 Seasons   →  2    |  seasons

### 8. Cleaning and Enriching the Genre Column
- Removed spacing inconsistencies in the `listed_in` column.
- Engineered a new feature: **`genre_count`** — the number of genres assigned to each title.

### 9. Correcting Data Types
- Converted columns to their appropriate data types (e.g., integers, datetime, strings) for accurate downstream analysis.

### 10. Dropping Unnecessary Columns
- Removed columns that added no analytical value, reducing noise in the dataset.



## ✅ Results Summary

| Metric |                | Before Cleaning |   | After Cleaning |
|--------|                |-----------------|   |----------------|
| Shape |                 |8,790 × 10 |         | 8,790 × 14 |
| Missing Values |        | Present |           |**0** |
| Duplicate Rows |        | Present |           |**0** |
| Date Format |           |Inconsistent |       |DD-MM-YYYY |
| Duration |              |Single column |      |Split into 2 columns |
| Genre Count |           | Not available |     | Engineered feature added |


## ⚙️ Setup & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/netflix-data-cleaning.git
cd netflix-data-cleaning
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Cleaning Script

```bash
python "Python code for cleaning and preprocessing.py"
```

The cleaned dataset will be saved as:
- `netflix_cleaned.csv`
- `netflix_cleaned.xlsx`


## 📦 Requirements

pandas
numpy
openpyxl

> Install all at once: `pip install -r requirements.txt`


## 📸 Screenshots

output screenshots are available in the `screenshots/` folder, covering each cleaning stage from raw data to final output.


## 🔍 Project Outcome

The Netflix dataset was successfully cleaned and preprocessed using both **Excel** and **Python (Pandas)**. The final dataset is:

- ✅ Free of missing values and duplicates
- ✅ Consistently formatted and typed
- ✅ Enriched with engineered features (`genre_count`, `duration_value`, `duration_unit`)
- ✅ Ready for exploratory data analysis (EDA), visualization, or machine learning pipelines


