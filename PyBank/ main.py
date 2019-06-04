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
# in later calculations
dates = []
full_date = []
months = []
monthly_pl_change = []
total_pl = 0
month_2_month_changes = []
greatest_change = []
greatest_increase = 0
greatest_increase_date = []
greatest_decrease = 0
greatest_decrease_date = []
# Opening the PyBank .csv file and initializing the variable, csvfile, with it.
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile)
    # Looping through the entries in csvreader, appending the dates to a list and adding each P&L
    # to total_p_l
    for entry in csvreader:
        dates.append(entry)
        if 'Profit/Losses' not in entry[1]:
            monthly_pl_change.append(int(entry[1]))
            total_pl += int(entry[1])
    # Looping through the dates list, adding the full dates to a list as well as splitting the name
    # of the month and appending the splits into the months list
    for date in dates:
        if 'Date' not in date:
            full_date.append(date[0])
            months.append((date[0].split("-")[0]))
    # Looping through monthly_pl_change in order to find the absolute value difference
    # between each value and the next so that the average of the changes in "Profit/Losses" over
    # the entire period can be calculated
    for i in range(len(monthly_pl_change) - 1):
            month_2_month_changes.append(abs(monthly_pl_change[i] -
            monthly_pl_change[i + 1]))
    #Looping through monthly_pl_change in order to calculate the change in P&L between each month
    # and the next
    for i in range(len(monthly_pl_change) - 1):
            greatest_change.append((monthly_pl_change[i + 1] -
            monthly_pl_change[i]))
    # Looping through greatest_change in order to determine the greatest increase and decrease
    # experienced between months
    for i in range(len(greatest_change)):
        if greatest_change[i] > greatest_increase:
            greatest_increase = greatest_change[i]
            greatest_increase_date = full_date[i + 1]
        elif greatest_change[i] < greatest_decrease:
            greatest_decrease = greatest_change[i]
            greatest_decrease_date = full_date[i + 1]
# Printing statements that answer the questions of the PyBank dataset analysis 
number_of_months = len(months)
average_change = (sum(month_2_month_changes) / len(month_2_month_changes))
print(f'There are {number_of_months} months included in the PyBank dataset.')
print(f'The net total amount of "Profits and Losses" over the entire period is ${total_pl}.')
print(f'The average of the changes in "Profit/Losses" over the entire period is \
${int(average_change)}.')
print(f'The greatest increase in "Profits and Losses" over the entire period was \
${greatest_increase} and occured during {greatest_increase_date}.')
print(f'The greatest decrease in "Profits and Losses" over the entire period was \
${greatest_decrease} and occured during {greatest_decrease_date}.')
# Creating a text document that will store my analysis of the PyBank dataset
with open('Kylies_PyBank_Analysis.txt', 'w') as gen_file:
  lines = [f'There are {number_of_months} months included in the PyBank dataset.'
  f'\nThe net total amount of "Profits and Losses" over the entire period is ${total_pl}.'
  f'\nThe average of the changes in "Profit/Losses" over the entire period is ${int(average_change)}.'
  f'\nThe greatest increase in "Profits and Losses" over the entire period was ${greatest_increase} and occured during {greatest_increase_date}.'
  f'\nThe greatest decrease in "Profits and Losses" over the entire period was ${greatest_decrease} and occured during {greatest_decrease_date}.']
  gen_file.writelines(lines)
