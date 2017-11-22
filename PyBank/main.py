#PyBank Assignment

#import modules
import os
import csv

#create date and revenue lists
date = []
revenue = []

#read in csv file and append each column into lists
with open("budget_data_1.csv", newline= '') as file1:
    budgetfile = csv.reader(file1, delimiter= ',')
    next(budgetfile)
    for lines in budgetfile:
        date.append(lines[0])
        revenue.append(int(lines[1]))
#print(len(date))

#check that each month is unique and get the total number of months
#--------TOTAL NUMBER OF MONTHS (calc)
unique_count_months = []
for x in date: 
    if x not in unique_count_months:
        unique_count_months.append(x)
    else:
        continue
#print(len(unique_count_months))
#print(int(len(unique_count_months)-1))

#--------TOTAL REVENUE (calc)
#total revenue
total_rev = 0
for x in revenue:
    total_rev = total_rev + x
#print(total_rev)

#function to get differences in revenue for each month
def rev_diff(prev_month,curr_month):
    return(curr_month - prev_month)

#apply function to get a list of differences in revenue between months
total_rev_diff = []
for z in range(len(revenue)):
    if z == len(revenue) - 1:
        break
    diff = rev_diff(revenue[z],revenue[z+1])
    total_rev_diff.append(diff)
#print(total_rev_diff)


#---------AVERAGE CHANGE IN REVENUE (calc)
#total sum of differences over the total number of differences.  This is one less than total number of months.
avg_rev_change = int(sum(total_rev_diff)/(len(revenue)-1))

#insert 0 to the 'all_rev_diff' so that when combined with 'date' list, total rows will match
#also, the first difference starts at the 2nd month, not the 1st month.
#use zip function to get a list of tuples
total_rev_diff.insert(0,0)
combined_data = zip(date,total_rev_diff)

#convert list of tuples to dictionary
combined_data_dict = dict(combined_data)
#print(combined_data_dict)


#---------GREATEST INCREASE in REVENUE (calc)
max_value = max(combined_data_dict.values())
max_date = max(combined_data_dict, key=combined_data_dict.get)

#---------GREATEST DECREASE in REVENUE (calc)
min_value = min(combined_data_dict.values())
min_date = min(combined_data_dict, key=combined_data_dict.get)



#---------SUMMARY OF RESULTS
print('')
print("Financial Analysis")
print("-----------------------------------")
print("Total Months: " + str(len(unique_count_months)))
print("Total Revenue:  " + "$" +str(total_rev))
print("Average Revenue Change:  " + "$" +str(avg_rev_change))
print("Greatest Increase in Revenue:  " + max_date + " ($" + str(max_value) + ")")
print("Greatest Decrease in Revenue:  " + min_date + " ($" + str(min_value) + ")")
print('')
