import os as os
import pandas as pd
csvpath_2 = os.path.join("Resources", "election_data.csv")

df = pd.read_csv("resources/election_data.csv")
# df.info()
total = len(df)
# print(df.keys())
candidate_count_df = (df["Candidate"].value_counts(ascending = False))
print("Election Results")
print("-------------------------")
print("Total Votes: {} ".format(total))
print("-------------------------")
for candidate in sorted(candidate_count_df.items()):
    print("{}: {}% ({})".format(candidate[0], round(candidate[1]/total * 100, 2),candidate[1]))
print("-------------------------")
# next returns only the first item in a list
print("Winner: {}".format((next(candidate_count_df.items()) [0])))
print("-------------------------")
