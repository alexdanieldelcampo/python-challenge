import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

total_months = 0 
total = 0
change = []

last_chg = 0
biggest_inc = 0
biggest_dcr = 0
max_month = ''
min_month = ''

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
    
        total_months += 1
        total += int(row[1])
        change.append(int(row[1]))
        
        # had to find a way to cycle through the csv file and store infor from the previous list.
        if int(row[1]) - last_chg > biggest_inc:
            biggest_inc = int(row[1]) - last_chg
            max_month = row[0]
        elif int(row[1]) - last_chg < biggest_dcr:
            biggest_dcr = int(row[1]) - last_chg
            min_month = row[0]
        
        # stored variable for finding the greatest increase/decrease
        last_chg = int(row[1])
    
    #used this 'for loop' to find the average change bewteen all months
    difference = [j-i for i, j in zip(change[:-1], change[1:])]
    avg_change = round(sum(difference)/len(difference),2)
   
    
analysis = '/Users/Alexander/DataClass/python-challenge/PyBank/analysis/analysis.txt'
with open(analysis, 'w') as text:
    
    text.write(f"Financial Analysis \n---------------------------- \nTotal Months: {total_months} \nTotal: {total} \nAverage  Change: ${avg_change} \nGreatest Increase in Profits: {max_month} (${biggest_inc}) \nGreatest Decrease in Profits: {min_month} (${biggest_dcr})")