import os
import csv

file = os.path.join('Resources','election_data.csv')

candidates_list=[]
unique_candidates_list=[]
vote_count_list=[]
vote_percent_list=[]

count=0

with open (file,newline="") as csvfile:
    reader=csv.reader(csvfile, delimiter=",")
    header=next(reader)

    for row in reader :

        count = count+1
        candidates_list.append(row[2])

    for a in set (candidates_list):
        unique_candidates_list.append(a)
        b=candidates_list.count(a)
        vote_count_list.append(b)
        c=(b/count)*100
        vote_percent_list.append(c)
    
    winner_vote_count=max(vote_count_list)
    winner=unique_candidates_list[vote_count_list.index(winner_vote_count)]


print('---------------------')
print('ELECTION RESULTS')
print('---------------------')
print('TOTAL VOTES : ' + str(count))
for i in range(len(unique_candidates_list)):
    print(unique_candidates_list[i] + ': ' + str(vote_percent_list[i]) + '% ('+str(vote_count_list[i])+')')
print('---------------------')
print('THE WINNER IS : '+ winner)
print('---------------------')

with open('election_results.txt','w') as text:
    text.write('---------------------\n')
    text.write('ELECTION RESULTS\n')
    text.write('---------------------\n')
    text.write('TOTAL VOTES : ' + str(count)+ '\n')
    for i in range(len(unique_candidates_list)):
        text.write(unique_candidates_list[i] + ': ' + str(vote_percent_list[i]) + '% ('+str(vote_count_list[i])+')\n')
    text.write('---------------------\n')
    text.write('THE WINNER IS : '+ winner + '\n')
    text.write('---------------------\n')
