'''
This Python script checks meeting attendance by comparing two Excel sheets: 
one with the initial attendance list and one with the final list. It identifies 
attendees who left early and writes their names to a new Excel file.

Usage:
1. Ensure you have two Excel files: one for initial attendance and one for final attendance.
2. Specify the file paths and the column name that uniquely identifies each attendee.
3. Run the script. The missing attendees will be saved to 'missing_entries.xlsx'.
  
Required Libraries:  
- pandas (install via 'pip install pandas')
- openpyxl (install via 'pip install openpyxl')

'''
     
import pandas as pd

#Load the Excel files
file1 = r'C:\Users\AIX\Downloads\test1.xlsx' 
file2 = r'C:\Users\AIX\Downloads\test2.xlsx'

#'identifier_column' with the column name that uniquely identifies each attendee
identifier_column = 'Name'

#Read the Excel files into DataFrames
df_start = pd.read_excel(file1)
df_end = pd.read_excel(file2)

#Find entries in the first file but not in the second
missing_entries = df_start[~df_start[identifier_column].isin(df_end[identifier_column])]

# Save the missing entries to a new CSV file
missing_entries.to_csv('missing_entries.csv', index=False)

#This will show that the operation is successful
print("Comparison complete. Missing entries have been saved to 'missing_entries.csv'.")
