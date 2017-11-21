import os
import csv

#allbudget = []
date = []
revenue = []
#budget1_csv_path = os.path.join("data","budget_data_1.csv")

with open("budget_data_1.csv", newline= '') as file1:
    budget1file = csv.reader(file1, delimiter= ',')
    next(budget1file)
    for lines in budget1file:
        date.append(lines[0])
        revenue.append(int(lines[1]))
    #print(date)
with open("budget_data_2.csv", newline= '') as file2:
    budget2file = csv.reader(file2, delimiter= ',')
    next(budget2file)
    for line in budget2file:
        date.append(line[0])
        revenue.append(int(line[1]))
print(len(date))

#total months
#print(len(date))
#dateSet = set(date)
#print(len(set(date)))
unique_date = []
for x in date: 
    if x not in unique_date:
        unique_date.append(x)
    else:
        continue
print(len(unique_date))
        
#total revenue
totalrev = 0
for x in revenue:
    totalrev = totalrev + x
print(totalrev)

averagerev = totalrev/(len(date))
print(averagerev)

#b = {allbudget[i]: allbudget[i+1] for i in range(0, 1)}
#print(b)
#total counts
#total_months = 0
#for i in allbudget:
#    

#    print(i[0])
