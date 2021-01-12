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
netprofit = []
file_to_output = os.path.join("pyBank.txt")

# open the cvs file to read the data
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # don't need the print(csv_header), but loop through reading each row
    for row in csvreader:
        monthcount.append(row[0])
        netprofit.append(int(row[1]))

# calculation for total months
total_months = (len(monthcount))

# calculation for net total amount of "profit/losses" over entire period
netprofit_total = sum(netprofit)

# calculate the changes in "profit/losses" over entire period, start with $ total 

#highest and lowest change
highest_change = max(netprofit)
lowest_change = min(netprofit)

#highest and lowest month
highest_month = netprofit.index(highest_change)
lowest_month = netprofit.index(lowest_change)

#now bestestest month
best = monthcount[highest_month]
worst = monthcount[lowest_month]

# check where I'm at, I have no idea what I was trying earlier
#I made it way too hard, success for total amount!
print("Financial Analysis")
print("-----------------------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${netprofit_total}')
print(f'Greatest Increase in Profits: {best} (${highest_change})')
print(f'Greatest Decrease in Losses: {worst} (${lowest_change})')

pyBank_output = os.path.join(".", "pyBank_output.txt")
with open(pyBank_output, "w") as new:
    new.write("Financial Analysis")
    new.write("-----------------------------------------------------")
    new.write(f'Total Months: {total_months}')
    new.write(f'Total: ${netprofit_total}')
    new.write(f'Greatest Increase in Profits: {best} (${highest_change})')
    new.write(f'Greatest Decrease in Losses: {worst} (${lowest_change})')