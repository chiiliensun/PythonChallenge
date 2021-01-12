#importing the modules
import os
import csv

# completing the path C:\Users\sun_c\Documents\Bootcamp\PythonChallenge\PythonChallenge\PyBank\Resources\budget_data.csvr
csvpath = os.path.join('PyBank/Resources', 'budget_data.csv')

# make the lists
total = []
months = []
month_change = []

# #stupic calculations
# def average (numbers):
#     total = 0.0
#     for number in numbers:
#         total += number
#     average_month = total/len(numbers)
#     return average_month

# open the cvs file to read the data
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # print(csv_header)
    for row in csvreader:
        months.append(row[0])
        total.append(row[1])
        month_change.append(int(row[1]))

print(f'Total Months: {len(months)}')

