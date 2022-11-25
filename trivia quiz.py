import pandas as pd
count=0
data = pd.read_csv("C:\\Users\\sastr\\OneDrive\\Documents\\trivia quiz.csv",encoding ='latin-1')
print("-----------------------------------------------------Round 1 -------------------------------------------------------------\n"
                               "Round 1 has 5 questions and 10 points will be awarded for each correct answer"
)

for i in range (5):
    q = data.sample()
    print(q['Questions'])
    print("Your Answer - ",end = ' ')
    a = input()
    b= str(q.iloc[0,1])
    if(a.lower()==b.lower()):
        print("Corret Answer\n")
        count=count+10
    else:
        print("Wrong Answer\n")
        count=count+0
print("Your score at the end of round 1 : ",count)
i=0
print("\n")
print("-----------------------------------------------------Round 2 -------------------------------------------------------------\n"
                               "Round 2 has 5 questions and 20 points will be awarded for each correct answer"
)
for i in range (5,9):
    q = data 
    print(q['Questions'][i])
    print("Your Answer - ",end = ' ')
    a = input()
    b= str(q.iloc[0,1])
    if(a.lower()==b.lower()):
        print("Corret Answer\n")
        count=count+20
    else:
        print("Wrong Answer\n")
        count=count+0
print("Your score at the end of round 2 : ",count)
i=0
print("\n")
print("-----------------------------------------------------Round 3 -------------------------------------------------------------\n"
                               "Round 3 has 3 questions and 40 points will be awarded for each correct answer\n"
)
for i in range (10,13):
    q = data 
    print(q['Questions'][i])
    print("Your Answer - ",end = ' ')
    a = input()
    b= str(q.iloc[0,1])
    if(a.lower()==b.lower()):
        print("Corret Answer\n")
        count=count+40
    else:
        print("Wrong Answer\n")
        count=count+0
print("Your Total score : ",count)
