# Exploratory Data Analysis

## Exploratory Data Analysis (EDA)

## Project Overview
This project performs Exploratory Data Analysis (EDA) on a book dataset collected through web scraping. The analysis aims to understand the dataset, identify patterns and trends, detect anomalies, and prepare the data for further analysis.

## Objectives
- Explore the dataset structure.
- Understand variables and data types.
- Check for missing values and duplicate records.
- Clean and prepare the data.
- Generate descriptive statistics.
- Visualize the data using charts.
- Identify trends and insights.

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Visual Studio Code

## Dataset Information
- **Total Records:** 20
- **Total Columns:** 4

### Dataset Columns
| Column | Description |
|--------|-------------|
| Title | Name of the book |
| Price | Price of the book |
| Availability | Stock availability |
| Rating | Book rating |

## Data Preprocessing
The following preprocessing steps were performed:
- Imported the dataset.
- Checked the dataset structure.
- Verified data types.
- Checked for missing values.
- Checked for duplicate records.
- Converted the **Price** column from text to numeric format.

## Exploratory Data Analysis
The following analyses were performed:
- Dataset overview
- Missing value analysis
- Duplicate record analysis
- Descriptive statistics
- Price distribution using Histogram
- Outlier detection using Box Plot
- Rating distribution using Bar Chart

## Key Findings
- The dataset contains **20 books**.
- No missing values were found.
- No duplicate records were found.
- The **Price** column was successfully converted to numeric format.
- The average book price is **£38.05**.
- Book prices range from **£13.99** to **£57.25**.
- No significant outliers were detected.
- All books are currently marked as **In Stock**.

## Files Included
```
EDA/
│── dataset.csv
│── EDA.py
│── README.md
│── price_histogram.png
│── price_boxplot.png
└── rating_distribution.png
```

## Conclusion
The Exploratory Data Analysis successfully examined the dataset, verified data quality, and generated meaningful visualizations. The dataset is clean, contains no missing or duplicate values, and is ready for further analysis or visualization.

## Author
**Siva Sankari**
