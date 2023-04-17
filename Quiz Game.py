questions = ["What does RAM stands for?","What does ROM stands for","What is not the part of CPU?"]
op1 = ["a.Random Access Memory","b.Read only Memory","c.Required as Memory"]
op2 =["a.Random Access Memory","b.Read only Memory","c.Rwite only Memory"]
op3 = ["a.ALU","b.RCU","c.CU"]
options = [op1,op2,op3]
ans1 = 'a'
ans2 = 'b'
ans3 = 'b'
answers = [ans1,ans2,ans3]
score = 0
print("___________________________________________________________________")
print("___________________________________________________________________")
for i in range(0,3):
    print(questions[i]+"\n")
    print(options[i])
    answer = input("Answer: ")
    
    if(answer == answers[i]):
        print("You got it!")
        score += 1
        print("------------------------------------------------------------------------")
        continue
    else:
        j = 0
        while(j <1):
            print("Try again")
            print(questions[i]+"\n")
            print(options[i])
            answer = input("Answer: ")
            if(answer == answers[i]):
                print("You got it second time!")
                score += 0.5 
                break  
            else:
                print("WRONG! You lost 1 point")
                j=j+1
                continue
        continue
print("Your score is "+str(score))        
        
