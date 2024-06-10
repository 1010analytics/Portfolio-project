
from time import time
sentence= "python is core language in the field of data science"


print(">>",sentence)
start= time()

givensen = input(">> ")
end= time()

total_charac = len(sentence)
total_given_charac= len(givensen)
correct_charac = 0

r= min(total_charac, total_given_charac)

for i in range(r):
    if sentence[i]==givensen[i]:
        correct_charac +=1

time_taken =round((end-start),2)

##click per secc (CPS)
#cps= round(correct_charac/time_taken)

## click per minute (cpm)
cpm= round((int(correct_charac)/int(time_taken))*60)

## word per minute (wpm)
## let us consider that one word contain 4 characters.
wpm= cpm/4

## Now to define accuracy
acc= round((correct_charac/total_charac)*100)

print("CPM", cpm)
print("WPM", wpm)
print("Acc", acc)
print("correct charac", correct_charac)
print("time_taken", time_taken)