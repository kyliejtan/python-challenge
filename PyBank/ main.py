# Your task is to create a Python script that analyzes the records to calculate
# each of the following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal
# and export a text file with the results
import csv
# Initializing the variable cvspath with the name of the PyBank .csv file
csvpath = "03-Python_homework_PyBank_Resources_budget_data.csv"
# Initializing some empty lists and variables set to 0 so that they can be used to store values
# from later calculations
dates = []
months = []
monthly_pl_change_amounts = []
total_pl = 0
month_2_month_changes = []
# Opening the PyBank .csv file and initializing the variable, csvfile, with it.
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile)
    # print(list(csvreader))
    # Looping through the entries in csvreader, appending the dates to a list and adding each P&L
    # to total_p_l
    for entry in csvreader:
        dates.append(entry)
        if 'Profit/Losses' not in entry[1]:
            monthly_pl_change_amounts.append(int(entry[1]))
            total_pl += int(entry[1])
    # Looping through monthly_pl_change_amounts in order to find the absolute value difference
    # between each value and the next so that the average of the changes in "Profit/Losses" over
    # the entire period can be calculated
    for i in range(len(monthly_pl_change_amounts) - 1):
            month_2_month_changes.append(abs(monthly_pl_change_amounts[i] -
            monthly_pl_change_amounts[i + 1]))
    # Looping through the dates list, splitting the name of the month and appending the splits into
    # the months list
    for date in dates:
        if 'Date' not in date:
             months.append((date[0].split("-")[0]))
# Printing statements of how many months are included in the dataset, and the net total amount of
# "Profits and Losses" over the entire period
number_of_months = len(months)
average_change = (sum(month_2_month_changes) / len(month_2_month_changes))
print(f'There are {number_of_months} included in the PyBank dataset')
print(f'The net total amount of "Profits and Losses" over the entire period is ${total_pl}')
print(f'The average of the changes in "Profit/Losses" over the entire period is \
${int(average_change)}')
