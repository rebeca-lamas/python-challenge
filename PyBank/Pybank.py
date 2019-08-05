import csv
import os
import numpy as np

# Def totalMonths():
csvpath = os.path.join('..', 'HW 3', 'budget_data.csv')
    
with open(csvpath, newline='') as csvfile:
    
 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    Profits = []
    B = []
    C = []
    dates = []
    #copies csv to a list
    for row in csvreader:
        Profits.append(row[1]) #adds only profits
        B.append(row[1]) #adds only profits
        C.append(row[1]) #adds only profits
        dates.append(row[0]) #adds only dates
        # print(row)

    # to find difference doing next line - current line. 
    # B is an array of current lines, so we delete last item
    del B[-1]     

    # C is an array of next lines, so we delete first item
    del C[0]

    #converts lists to numphy array and to specified data types
    Profits = np.array(Profits, dtype=float)
    B = np.array(B, dtype=float)
    C = np.array(C, dtype=float)
    dates = np.array(dates, dtype=str)
    
    #outputs difference from C - B or next line - current linem as an array
    difference = np.subtract(C,B)
    averageChange = np.average(difference) #calculates average of the difference array
    totalMonths = len(dates) #length of dates array = total months. works since no dulplicate months in data
    totalProfit = sum(Profits) #calculates sum of profits 
    
    maximum = max(difference) #finds max of differnce array
    index_of_maximum = np.where(difference == maximum) #locates the index of max on difference array
    i = index_of_maximum[0] #index_of_maximum outputs an array of info about index. we only want its location = first element in that array
    i = i + 1 #add one to the index location since we need to find the corresponding date. difference array is one element shorter than profits array

    #same logic from max applies to min
    minimum = min(difference)
    index_of_minimum = np.where(difference == minimum)
    j = index_of_minimum[0]
    j = j + 1
    
    #prints report
    print("Financial Analysis")
    print("-------------------------------")
    print(f'Total Months: {totalMonths}')
    print(f'Total: ${"%.0f" % totalProfit}')
    print(f'Average Change: $ { "%.2f" % averageChange}')
    print(f'Greatest Increase in Profits: {dates[i]} (${"%.0f" % maximum})')
    print(f'Greatest Decrease in Profits: {dates[j]} (${"%.0f" % minimum})')