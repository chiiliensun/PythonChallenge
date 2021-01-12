# Need to import the os module that will allow the creation of file paths across operating systems
# Import for reading csv file, for budget.data.csv
import os
import csv

# print("---My Prin---")
# print(os.getcwd()) where is my directory at?
# print("--end--")
# #finally success! Missed the PyBank/Resources

# completing the path C:\Users\sun_c\Documents\Bootcamp\PythonChallenge\PythonChallenge\PyBank\Resources\budget_data.csv
csvpath = os.path.join("PyBank/Resources", "budget_data.csv") 

# testing and plain reading of CSV files, will be using later but need to parcel it out
# with open(csvpath, newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     csv_header = next(csvreader)
#     print(csv_header) 

# set the lists
monthcount = []
netchange = []

# open the cvs file to read the data
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # don't need the print(csv_header), but loop through reading each row
    for row in csvreader:
        monthcount.append(row[0])
        netchange.append(int(row[1]))

#calculation for total months
total_months = (len(monthcount))

# check where I'm at
print(f'Total Months: {total_months}')

