scores = [78, 92, 65, 88, 100, 54, 91, 73]
total=0
average=0
count_90=0
highest=scores[0]
for i in scores:
    total+=i
    average=total/len(scores)
    if i>=90:
        count_90+=1
    if i>highest:
        highest=i
print("The total score is:", total)
print("Average score:", average)
print("The number of students with scores 90 or above is:", count_90)
print("Max score:", highest)




