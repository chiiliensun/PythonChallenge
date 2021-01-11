# Python Day 2, 08-Ins_ReadCSV. Need to import the os module that will allow the creation of file paths across operating systems
# Import for reading csv file, for budget.data.csv
import os
import csv

# completing the path C:\Users\sun_c\Documents\Bootcamp\PythonChallenge\PythonChallenge\PyBank\Resources\budget_data.csv
csvpath = os.path.join("PyBank/Resources", "budget_data.csv") 

# testing and plain reading of CSV files
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(csv_header) 
# 
# 
# 
# 
