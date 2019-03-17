#import modules
import os
import csv

#set the file path so it is compatible with all operating systems
file_path = os.path.join(".", "election_data.csv")

#initialize variables
votecounter = 0
all_candidates = []
unique_candidates = []
winning_votes = 0

#open the file, user csv.reader to parse the contents, and skip the header during further analysis
with open(file_path) as csvfile:
    filereader = csv.reader(csvfile, delimiter = ",")
    header = next(filereader)

    #loop through each row to count and store the total number of vote and create a list of all votes by candidate name
    for row in filereader:
        votecounter += 1
        all_candidates.append(row[2])
    
    #loop through the list of each vote by name, and create a new list of unique candidates
    for x in all_candidates:
        if x not in unique_candidates:
            unique_candidates.append(x)

    #create an empty list based on the number of candidates to store each candidates total vote counts
    total_vote_list = [0 for name in unique_candidates]

    #loop throught the list of all votes by candidate name and store total votes per unique name in the empty list
    #the order of this list should match the order of the unique candidates list because they were both generated in the same way
    
    for i in range(len(total_vote_list)):
	    for name in all_candidates:
		    if name == unique_candidates[i]:
			    total_vote_list[i] += 1          

    #calculate the percentages of total votes for each candidates and store them in a list
    candidate_percentages = [(votes / votecounter * 100) for votes in total_vote_list]

    #determine the highest number of votes recieved
    for x in total_vote_list:
        if x > winning_votes:
            winning_votes = x

    #find the index position of the highest number of votes and match it with an index value from the unique voters list to find the winners name
    index_of_winner = total_vote_list.index(winning_votes)

    winner = unique_candidates[index_of_winner]

#print the results and assign each line a variable so they can be written to a text file
aa = ("Election Results"'\n'"--------------------------- ")
bb = ("Total Votes: " + str(votecounter)+ " ")
cc = ("---------------------------")
dd = (f"{unique_candidates[0]}: {round(candidate_percentages[0],3)}% ({total_vote_list[0]}) ")
ee = (f"{unique_candidates[1]}: {round(candidate_percentages[1],3)}% ({total_vote_list[1]}) ")
ff = (f"{unique_candidates[2]}: {round(candidate_percentages[2],3)}% ({total_vote_list[2]}) ")
gg = (f"{unique_candidates[3]}: {round(candidate_percentages[3],3)}% ({total_vote_list[3]}) ")
hh = ("--------------------------- ")
ii = (f"Winner: {winner}"'\n'"---------------------------")

total_print = [aa,bb,cc,dd,ee,ff,gg,hh,ii]

print("\n".join(total_print))

#print the results to a text file
final_path = os.path.join(".", "final_analysis.txt")
with open(final_path, "w", newline="") as textfile:
    textfile.writelines(total_print)