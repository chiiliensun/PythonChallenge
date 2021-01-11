#importing the modules
import os
import csv
# print("---My Prin---")
# print(os.getcwd()) where is my directory at?
# print("--end--")

#Didn't understand the path, found that needing to add where in PythonChallenge folder that would find the Resources folder
csvpath = os.path.join('PyBank/Resources', 'budget_data.csv')

#ensuring that my csv file is found and imported
#finally success! Missed the PyBank/Resources
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(csv_header)

