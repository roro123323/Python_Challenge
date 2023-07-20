# Author: Roel De Los Santos
# Title: PyBank - Module 3 assignment
# Date : 7/16/2023

import os
import csv 

# Define the file path
p = 'Resources/budget_data.csv'


# Initialize variables 
count = 0
totPL = 0
mtmchanges = []

with open(p, 'r') as budget_data:
    readcsv = csv.reader(budget_data, delimiter= ',')
    # Handle the header
    header = next(readcsv)
    prevPL = 0 
     # Loop rows 
    for row in readcsv:
        profit_loss = int(row[1])
        count += 1 
        totPL += profit_loss
        mtmchanges.append([row[0], profit_loss - prevPL])
        prevPL = profit_loss 
# use lambda for function on list of list 
max_change = max(mtmchanges, key = lambda x: x[1])
min_change = min(mtmchanges, key = lambda x: x[1])  

# Average change 
average_change = sum(map(lambda x: int(x[1]), mtmchanges)) / count 

print('-------------------------------')
print('Financial Analysis')
print('-------------------------------')
print('Total Months : ' + str(count))
print('Total Profits : ' + '$' + str(totPL))
print('Average Change : ' + '$' + str(int(average_change)))
print('Greatest Increase in Profits : ' + str(max_change[0]) + ' ($' + str(max_change[1]) + ')')
print('Greatest Decrease in Profits : ' + str(min_change[0]) + ' ($' + str(min_change[1]) + ')')
print('-------------------------------')

# Write Financial analysis summary to txt file 
outputfile = 'summary.txt'

#use '\n' to create a new line 
with open(outputfile, 'w') as output: 
    output.write('_'*50 + '\n')
    output.write('Financial Analysis\n')
    output.write('_'*50 + '\n')
    output.write(f'Total Months: {count}\n' ) 
    output.write(f'Total Profits: ${totPL}\n')
    output.write(f'Average Change: ${str(average_change)}\n')
    output.write(f'Greatest Increase in Profits:{max_change[0]} (${max_change[1]})\n')
    output.write(f'Greatest Decrease in Profits:{min_change[0]} (${min_change[1]})\n')
    output.write('_'*50 + '\n')


