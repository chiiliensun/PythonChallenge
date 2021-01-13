# Import for module and reading file, for budget.data.csv
import os
import csv

# complete the path
csvpath = os.path.join(os.getcwd(), 'PyBank/Resources' , 'budget_data.csv')

# set lists
monthcount = []
netprofit = []

#open the cvs file to read the data stored
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #print(csv_header)
    for row in csvreader:
        monthcount.append(row[0])
        netprofit.append(int(row[1]))

# calculate the total months
total_months = len(monthcount)

# calculate for net total on "Profit/Losses"
netprofit_total = sum(netprofit)

# set new list to hold the change calculation
profit_change = []
#start loop to calculate change, must minus one for first row
for i in range(len(netprofit)-1):
    change = netprofit[i+1] - netprofit[i]
    profit_change.append(change)

#average out the changes in "profit/losses"
average_change = sum(profit_change) / len(profit_change)

#highest and lowest change
highest_change = max(netprofit)
lowest_change = min(netprofit)

#highest and lowest month
highest_month = netprofit.index(highest_change)
lowest_month = netprofit.index(lowest_change)

#now bestestest month
best = monthcount[highest_month]
worst = monthcount[lowest_month]

#print statement for analysis
print("Financial Analysis")
print("-----------------------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${netprofit_total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {best} (${highest_change})')
print(f'Greatest Decrease in Losses: {worst} (${lowest_change})')

#file write
pyBank_output = os.path.join("Analysis" , "pyBank_output.txt")
with open(pyBank_output, "w") as new:
    new.write("Financial Analysis\n")
    new.write("-----------------------------------------------------\n")
    new.write(f'Total Months: {total_months}\n')
    new.write(f'Total: ${netprofit_total}\n')
    new.write(f'Average Change: ${average_change}\n')
    new.write(f'Greatest Increase in Profits: {best} (${highest_change})\n')
    new.write(f'Greatest Decrease in Losses: {worst} (${lowest_change})\n')
