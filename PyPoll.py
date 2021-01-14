# The data we need to retrieve is
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Get candidate options
candidate_options = []

# Declare empty dictionary
candidate_votes = {}

# Winning Candidate Count Ticker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file
    for row in file_reader:
        #Add to the toal vote count
        total_votes += 1

        # Print candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add names to candidate list
            candidate_options.append(candidate_name)
            #Track candidate vote count
            candidate_votes[candidate_name] = 0

        # Add candidate votes
        candidate_votes[candidate_name] += 1

    # Get candidate vote percentage
    for candidate_name in candidate_votes:
        # Get vote counts
        votes = candidate_votes[candidate_name]
        # Get percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Print the winner
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}&\n"
        f"-------------------------\n")
    print(winning_candidate_summary)



# 1. The total number of votes cast

# 2. A complete list of candidates who received votes

# 3. The percentage of votes each candidate won

# 4. The total number of votes each candidate won

# 5. The winner of the election based on popular votes