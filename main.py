# This is the file where I will keep all my code for the Module_3 assignment
import csv
import os

csvpath = csvpath = os.path.join("Resources", "pyban.csv")


with open('./resources/pybank.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    months_processed = []
    num_months = 0 
    total = 0
    previous_profit = 0
    changes = []
    grt_p = [0, ""]
    grt_d = [0, ""]
    for row in spamreader:
        # telling loop to ignore header row
        if num_months == 0:
            num_months = num_months + 1 
            continue
        profit_num = int(row[1])
        # reomoves duplicte rows if necessary
        if row[0] not in months_processed:
            num_months = num_months + 1 
            months_processed.append(row[0])
        # changed row to integer to run code!
        total = total + profit_num
        # for average of averages!
        if previous_profit != 0:
            change = profit_num - previous_profit
            changes.append(change)
            print(change)
             # for greatest increase and decrease
             # [0] sets for automatic change 
            if grt_p[0] < change:
                grt_p[0] = change
                grt_p[1] = row[0]
                print(row[0])
            if grt_d[0] > change:
                grt_d[0] = change 
                grt_d[1] = row[0]
                print(row[0])
        previous_profit = profit_num  
        # print(row)
        # print(row[0])
        # print(row[1])
    for column in row:
        print(column.replace('\t', ' '))
    print(num_months)
    print (total)
    average_change = sum(changes) / len(changes)
    print(round(average_change, 2))
    print(grt_p)
    print(grt_d)



    



