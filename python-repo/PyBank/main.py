import os
import csv

file = os.path.join('Resources','budget_data.csv')

profit=[]
monthly_change=[]
date=[]

count=0
initial_profit=0
total_profit=0
total_change=0
total_change_profits=0

with open (file,newline="") as csvfile:
    reader=csv.reader(csvfile, delimiter=",")
    header=next(reader)
    for row in reader :
        
        count=count+1
        date.append(row[0])
       
        profit.append(row[1])
        total_profit= total_profit + int(row[1])
        last_profit=int(row[1])
        monthly_profit=last_profit-initial_profit
        monthly_change.append(monthly_profit)
        total_change_profits=total_change_profits+monthly_profit
        initial_profit=last_profit
        
        average_change=(total_change_profits/count)
        max_increase= max(monthly_change)
        max_decrease= min(monthly_change)

        max_date=date[monthly_change.index(max_increase)]
        min_date=date[monthly_change.index(max_decrease)]


print('-------------------------------------------')
print('Financial Analysis')
print('-------------------------------------------')
print('Total Months' + str(count))
print('Total Profits'+ '$' + str(total_profit))
print('Average Change' + '$' + str(average_change))
print('Greatest Profit Increase:' + str(max_date)+ "($"+str(max_increase)+')')
print('Greatest Profit Decrease:' + str(min_date)+ "($"+str(max_decrease)+')')
print('-------------------------------------------')

with open ('financial_analysis.txt','w') as text:
    text.write('-------------------------------------------')
    text.write('Financial Analysis')
    text.write('-------------------------------------------')
    text.write('Total Months' + str(count))
    text.write('Total Profits'+ '$' + str(total_profit))
    text.write('Average Change' + '$' + str(average_change))
    text.write('Greatest Profit Increase:' + str(max_date)+ "($"+str(max_increase)+')')
    text.write('Greatest Profit Decrease:' + str(min_date)+ "($"+str(max_decrease)+')')
    text.write('-------------------------------------------')