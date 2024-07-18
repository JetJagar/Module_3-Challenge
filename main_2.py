import os as os
import pandas as pd
csvpath_2 = os.path.join("Resources", "election_data.csv")

df = pd.read_csv("resources/election_data.csv")
df.info()
total = len(df)
print(df.keys())
candidate_count_df = (df["Candidate"].value_counts(ascending = False))
winner = True
winner_name = ""
for candidate in candidate_count_df.items():
    if winner: 
        winner_name  = candidate[0]
        winner = False    
    print(candidate[0])
    print(candidate[1])
    print(round(candidate[1]/total * 100, 2))
print(winner_name)






# with open('./resources/election_data.csv', newline='') as csvfile_2:
#     electionreader = pd.read_csv(csvfile_2, delimiter= ',')
#     total_votes = 0
#     vote_count = []
    
#     for row in electionreader:
#         # loops through all rows to add up votes
#         if total_votes == 0:
#             total_votes = total_votes + 1
#             continue
        
#         # removes duplicate rows if necessary    
#         if row[0] not in vote_count:
#             total_votes = total_votes + 1 
#             vote_count.append(row[0]) 
#     print(total_votes)