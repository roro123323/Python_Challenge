# Author: Roel De Los Santos
# Date: 07/18/2023
# Topic: Module 3 PyPoll 

import csv

# define file path
#p = '/Users/roeldelossantos/Desktop/Module_3/election_data.csv'
p = 'Resources/budget_data.csv'

tVotes = 0
vpc = {}

# read csv file
with open(p,'r') as election_data:
    readcsv = csv.reader(election_data, delimiter=',')
    # skips the header
    header = next(readcsv)

    for row in readcsv:
        tVotes += 1 
        if row[2] in vpc:
            vpc[row[2]] += 1
        else:
            vpc[row[2]] = 1     
print("Election Results")
print('-' * 50, '\n')
print('Total Votes: ' + str(tVotes))
print('-' * 50, '\n')
for k, v in vpc.items():
    pct = v /(sum(vpc.values())) 
    print(k, '{:.3%}'.format(pct)+ " (" +  str(v) + ")")
print('-' * 50, '\n')
print('Winner : ',max(vpc, key = lambda x: x[1]))    

# Output result to txt file
with open('election_results.txt', 'w') as t:
    t.write('Election Result'+ '\n')
    t.write('-' * 50+ '\n')
    t.write('Total Votes: ' + str(tVotes)+ '\n')
    t.write('-' * 50+ '\n')
    for k, v in vpc.items():
        pct = v /(sum(vpc.values())) 
        t.write(k + ': ' + '{:.3%}'.format(pct)+ " (" +  str(v) + ")"+ '\n')
        t.write('\n')
        #f.write(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    t.write('-' * 50+ '\n')
    t.write('Winner : '+ max(vpc, key = lambda x: x[1]))