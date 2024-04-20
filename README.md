# Toyota-Data-analysis
Complete analysis of Toyota Dataset



# Toyota Car Dataset Analysis

## Project Description

The Toyota Car Dataset Analysis project involves exploring and analyzing data related to Toyota cars using Python's Pandas library. The dataset contains information about various attributes of Toyota cars, including price, kilometers driven, horsepower, fuel type, doors count, and automatic transmission.

### Analyses:

1. **Data Exploration:**
   - The code loads the Toyota car dataset from a CSV file (`Toyota.csv`) and prints the first few rows to understand its structure.

2. **Data Cleaning:**
   - Junk values represented as '??' and '????' are identified in columns such as 'KM', 'HP', and 'FuelType'. These values are replaced with NaN (Not a Number) values to clean the data.

3. **Data Conversion:**
   - The 'Doors' column contains categorical values like 'three', 'four', 'five', etc. These values are converted to numerical values (3, 4, 5, etc.) for consistency and analysis.

4. **Data Transformation:**
   - The 'FuelType' column is converted to a categorical data type to improve memory efficiency and make analysis easier.

5. **Handling Missing Values:**
   - Missing values in the dataset are filled using the forward fill (`ffill`) method to replace NaN values with the previous valid values in the respective columns.

6. **Duplicate Rows Detection:**
   - The code checks for duplicate rows in the dataset and prints them if found, enabling data quality checks.

7. **Cross-Tabulation:**
   - Cross-tabulation is performed between the 'Automatic' and 'Doors' columns to analyze the distribution of automatic and manual cars based on the number of doors.

8. **Data Manipulation:**
   - The 'Age' column, representing the age of cars in months, is converted to years and rounded to one decimal place for clarity.
   - A new column 'price_class' is inserted to categorize car prices as 'Low', 'Mid', or 'High' based on predefined price ranges.

9. **Summary Statistics:**
   - Summary statistics, such as the count of cars in each price class and their respective percentages, are calculated and displayed.

### How to Use:

- Clone this repository and ensure that Python and required dependencies (Pandas, NumPy) are installed.
- Run the Python script (`analyze_toyota.py`) to perform the analyses described above.
- Review the results printed to the console to gain insights into the Toyota car dataset.

### Dataset Information:

- The Toyota car dataset contains information about various attributes of Toyota cars, including price, kilometers driven, horsepower, fuel type, doors count, automatic transmission, and age of the car.

---

This project aims to provide a comprehensive analysis of the Toyota car dataset, helping users understand the distribution and characteristics of Toyota cars based on different attributes.
