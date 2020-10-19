#import csv and os
import csv
import os

#define csv path and result output path
budget_file = os.path.join("Resources","budget_data.csv")
analysis = os.path.join("Analysis","financial analysis.txt")

#create list for month and profit/losses
PnL = []
date_list = []

#read csv file to grab date
with open(budget_file,"r") as csv_file:
    
    PL_List = csv.DictReader(csv_file, delimiter = ",")

    #write csv data into date and profit/losses lists    
    for row in PL_List:
            
            PnL.append(int(row["Profit/Losses"]))
            date_list.append(row["Date"])
#calculate number of months/total profit and loss/average/max increase/max decrease  
Months = len(PnL)
Total = sum(PnL)
Average = Total/Months
Max_Inc = max(PnL)
Max_Dec = min(PnL)

#find the index of max increase and decrease for looking up their dates
Inc_index = PnL.index(Max_Inc)
Dec_index = PnL.index(Max_Dec)

#find the increase and decrease date based on the index
Inc_date = date_list[Inc_index]
Dec_date = date_list[Dec_index]

#these are the result strings
Title = ("Financial Analysis")
Num = (f"Total Months: {Months}")
TotalPL = (f"Total: ${Total}")
Mean = (f"Average Change: ${Average}")
increase = (f"Greatest Increase in Profits: {Inc_date} ${Max_Inc}")
decrease = (f"Greatest Decrease in Profits: {Dec_date} ${Max_Dec}")

#create a text file and write output information, then save it to the correct path
f = open(analysis,"w")
f.write(f'{Title}\n-----------------------\n{Num}\n{TotalPL}\n{Mean}\n{increase}\n{decrease}')
f.close()