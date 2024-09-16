# Programming Assignment #3
This project demonstrates the use of the Python pandas library to explore and analyze a dataset containing various attributes of car models.
## Description
The project is divided into two parts:
1. Data Exploration: Loading the dataset into a pandas DataFrame and displaying initial and final rows to understand the structure of the data.
2. Data Manipulation: Extracting specific information using pandas operations, such as subsetting columns, filtering rows based on conditions, and retrieving targeted values for specific car models.
## Dependencies
- Pandas: Used for data manipulation and analysis.
- Cars.csv: Main source of data
- Windows 10
## Executing Program
## Problem 1
1. Importing Necessary Libraries: Import the pandas library, which is used for data manipulation and analysis.
2. Loading the CSV File into a DataFrame: Load the car data from a CSV file into a pandas DataFrame.
3. Displaying the First Five Rows: To inspect the first few rows of the data, we use the .head() method.
4. Displaying the Last Five Rows: To view the last few rows, we use the .tail() method.
## Problem 2
1. Displaying First Five Rows with Odd-Numbered Columns: Slicing the DataFrame using iloc, which allows positional indexing.
2. Extracting the Row with 'Mazda RX4': Filter the DataFrame based on the condition that the 'Model' column should be equal to 'Mazda RX4'.
3. Finding Cylinders for 'Camaro Z28': Filter the DataFrame to find this row and then access the 'cyl' value.
4. Finding Cylinders and Gear for Specific Models: Retrieve both the number of cylinders ('cyl') and gear type ('gear') for specific car models: "Mazda RX4 Wag", "Ford Pantera L", and "Honda Civic". Use the isin() method to filter the DataFrame for multiple models.
## Conclusion
- Problem 1: Focused on loading and exploring the dataset, helping to understand its structure.
- Problem 2: Focused on manipulating and extracting specific data from the DataFrame using pandas functionalities like slicing, filtering, and indexing.
## Authors
- Ryan Concepcion
## Version History
- 0.1
  - Initial release
## Acknowledgement
- Youtube
- Chatgpt
- Github

