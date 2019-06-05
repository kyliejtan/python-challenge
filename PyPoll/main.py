#Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# Importing the csv module
import csv
import pandas as pd
# Initializing a variable with the name of the PyPoll .csv file
csvpath = "03-Python_homework_PyPoll_Resources_election_data.csv"
# Opening the PyPoll .csv file and initializing the variable csvfile with it
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
# Loading the contents of the PyPoll .cs file into a Pandas dataframe
election_data = pd.read_csv("03-Python_homework_PyPoll_Resources_election_data.csv")
#print(election_data.head())
# Initializing
vote_counter = len(election_data['Voter ID'])
# Printing the total number of votes cast in this election
print(f'There were {vote_counter} votes cast in this election')
# Initializing an empty dictionary to hold the name of each of the candidates and the number of\
# votes they got as a key:value pair
candidate_names = {}
# Looping throught the election_data to check if the name of each candidate has already been added\
# to candidate_names. If it hasn't the loop will add the name and 1 as a key:value pair. If the\
# name already has been added, the loop will add one to that cnadidate's note tally
for i in range(len(election_data)):
    key = election_data['Candidate'][i]
    if key not in candidate_names:
        candidate_names.update({key: 1})
    elif key in candidate_names:
        candidate_names[key] += 1
# Printing candidate_name to see each candidate's name and how many votes they received.
candidate_list = list(candidate_names)
print(f'The candidates who ran in this election were {candidate_list[0]}, {candidate_list[1]},\
 {candidate_list[2]}, and {candidate_list[3]}')
# Calculating the percentage of votes that each candidate received
khan_percentage = int((candidate_names['Khan']/vote_counter) * 100)
correy_percentage = int((candidate_names['Correy']/vote_counter) * 100)
li_percentage = int((candidate_names['Li']/vote_counter) * 100)
otooley_percentage = int((candidate_names["O'Tooley"]/vote_counter) * 100)
# Printing the percentage of the vote that each candidate won
print(f'Khan received {khan_percentage}% of the vote')
print(f'Correy received {correy_percentage}% of the vote')
print(f'Li received {li_percentage}% of the vote')
print(f'O\'Tolley received {otooley_percentage}% of the vote')
#
khan_votes = candidate_names['Khan']
correy_votes = candidate_names['Correy']
li_votes = candidate_names['Li']
otooley_votes = candidate_names["O'Tooley"]
#
print(f'Khan received {khan_votes} votes.')
print(f'Correy received {correy_votes} votes.')
print(f'Li received {li_votes} votes.')
print(f"O'Tooley received {otooley_votes} votes.")
# Looping through candidate_name to initialize a variable with the key:value pair of the candidate\
# who won the election and how many votes they von with
winning_candidate = None
winning_votes = 0
for candidate, votes in candidate_names.items():
    if votes > winning_votes:
        winning_candidate = candidate
        winning_votes = votes
    else:
        continue
# Printing the winner of this election based on popular vote and how many votes they won with
print(f'The winner of this election was {winning_candidate}, who won with {winning_votes} votes.')
# Creating a .txt file to save the results of this analysis in
with open('Kylies_PyPoll_Analysis.txt', 'w') as gen_file:
    gen_file.write(f'There were {vote_counter} votes cast in this election.'
    f'\nThe candidates who ran in this election were {candidate_list[0]}, {candidate_list[1]},\
    {candidate_list[2]}, and {candidate_list[3]}.'
    f'\nKhan received {khan_percentage}% of the vote.'
    f'\nCorrey received {correy_percentage}% of the vote.'
    f'\nLi received {li_percentage}% of the vote.'
    f'\nO\'Tolley received {otooley_percentage}% of the vote.'
    f'\nKhan received {khan_votes} votes.'
    f'\nCorrey received {correy_votes} votes.'
    f'\nLi received {li_votes} votes.'
    f"\nO'Tooley received {otooley_votes} votes."
    f'\nThe winner of this election was {winning_candidate}, who won with {winning_votes} votes.')
