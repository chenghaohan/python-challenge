#import os to create path and pandas to analyze data
import pandas as pd
import os

#create input and output file paths 
election = os.path.join("Resources","election_data.csv")
output = os.path.join("Analysis","Election Results.txt")

#create data frame from the original csv file
results = pd.read_csv(election) 

#count lines to get total votes
total_votes = len(results)

#create a data frame that includes candidate names only, this is used to calculate their votes later
names = results.Candidate

#count the votes each candidate received and their percentage
votes = names.value_counts()
percentage = names.value_counts(normalize = True).mul(100).round(3).astype(str)+"%"

#create a data frame to present calculation and results
df = pd.DataFrame ({"Votes": votes,"Vote Percentage": percentage})
#the person who received most votes is the winner
winner = df['Votes'].idxmax()

#define our results 
title = 'Election Results'
total = (f"Total Votes: {total_votes}")
final = (f"Winner: {winner}")

#print out all our results 
print(title)
print("_ _ _ _ _ _ _ _ _ _ _ _ _")
print(total)
print("_ _ _ _ _ _ _ _ _ _ _ _ _")
print(df)
print("_ _ _ _ _ _ _ _ _ _ _ _ _")
print(final)
print("_ _ _ _ _ _ _ _ _ _ _ _ _")

#create a text file, write the results into text file and then save it to analysis folder
f = open(output,"w")
f.write(f"{title}\n_ _ _ _ _ _ _ _\n{total}\n\n{df}\n\n{final}\n")
f.close()