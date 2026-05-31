import pandas as pd
import numpy as np
import re

# -------------------------
# Load Dataset
# -------------------------
df = pd.read_csv("netflix.csv")

print("Dataset Shape:", df.shape)
print("\nColumn Data Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())


# -------------------------
# Rename Columns
# -------------------------
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)

print("\nColumns renamed")


# -------------------------
# Remove Extra Spaces
# -------------------------
str_cols = df.select_dtypes(include=["object", "string"]).columns

for col in str_cols:
    df[col] = df[col].str.strip()

print("Extra spaces removed")


# -------------------------
# Treat Null Values
# -------------------------
for col in str_cols:
    df[col] = df[col].fillna("Unknown")

print("Null values treated")


# -------------------------
# Populate Missing Rows
# -------------------------
df = df.ffill()

print("Missing rows populated")


# -------------------------
# Treat Duplicates
# -------------------------
duplicate_count = df.duplicated().sum()

print(f"\nDuplicates Found: {duplicate_count}")

df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

print("Duplicates removed")


# -------------------------
# Standardize Text
# -------------------------
df["type"] = df["type"].str.title()

df["director"] = (
    df["director"]
    .replace("Not Given", "Unknown")
)

df["country"] = (
    df["country"]
    .replace("Not Given", "Unknown")
    .str.title()
)

print("Text standardized")


# -------------------------
# Date Formatting
# -------------------------
df["date_added"] = pd.to_datetime(
    df["date_added"],
    format="%m/%d/%Y",
    errors="coerce"
)

# Extract year/month
df["year_added"] = (
    df["date_added"]
    .dt.year
    .astype("Int64")
)

df["month_added"] = (
    df["date_added"]
    .dt.month
    .astype("Int64")
)

# Reformat date
df["date_added"] = (
    df["date_added"]
    .dt.strftime("%d-%m-%Y")
    .fillna("Unknown")
)

print("Date cleaned")


# -------------------------
# Split Duration Column
# -------------------------
def parse_duration(d):
    match = re.match(
        r"(\d+)\s*(min|season|seasons)",
        str(d),
        re.IGNORECASE
    )

    if match:
        return int(match.group(1)), match.group(2).lower()

    return None, None


parsed = df["duration"].apply(parse_duration)

df["duration_value"] = pd.array(
    [x[0] for x in parsed],
    dtype="Int64"
)

df["duration_unit"] = [
    x[1] for x in parsed
]

df.drop(columns=["duration"], inplace=True)

print("Duration column split")


# -------------------------
# Standardize Genre Column
# -------------------------
df["listed_in"] = (
    df["listed_in"]
    .str.replace(r"\s*,\s*", ", ", regex=True)
)

df["genre_count"] = (
    df["listed_in"]
    .str.count(",") + 1
)

print("Genre column standardized")


# -------------------------
# Convert Data Types
# -------------------------
df["release_year"] = pd.to_numeric(
    df["release_year"],
    errors="coerce"
).astype("Int64")

print("Data types converted")


# -------------------------
# Drop Unneeded Columns
# -------------------------
drop_cols = ["description"]

existing_cols = [
    col for col in drop_cols
    if col in df.columns
]

df.drop(columns=existing_cols, inplace=True)

print("Unneeded columns dropped")


# -------------------------
# Final Null Check
# -------------------------
print("\nRemaining Null Values:")
print(df.isnull().sum())

print("\nFinal Dataset Shape:")
print(df.shape)


# -------------------------
# Save Cleaned Dataset
# -------------------------
df.to_csv(
    "netflix_cleaned.csv",
    index=False
)

df.to_excel(
    "netflix_cleaned.xlsx",
    index=False
)

print("\nCleaning Completed Successfully!")
