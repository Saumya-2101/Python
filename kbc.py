questions = [
    ["which language was used to built fb?" ,"python" , "french" , "javascript" , "php" , "none" ,4],

    ["which language was used to built fb?" ,"python" , "french" , "javascript" , "php" , "none" ,4],

    ["which language was used to built fb?" ,"python" , "french" , "javascript" , "php" , "none" ,4],

    ["which language was used to built fb?" ,"python" , "french" , "javascript" , "php" , "none" ,4],

    ["which language was used to built fb?" ,"python" , "french" , "javascript" , "php" , "none" ,4],

    ["which language was used to built fb?" ,"python" , "french" , "javascript" , "php" , "none" ,4],

    ["which language was used to built fb?" ,"python" , "french" , "javascript" , "php" , "none" ,4],

    ["which language was used to built fb?" ,"python" , "french" , "javascript" , "php" , "none" ,4],

    ["which language was used to built fb?" ,"python" , "french" , "javascript" , "php" , "none" ,4],

    ["which language was used to built fb?" ,"python" , "french" , "javascript" , "php" , "none" ,4],

    ["which language was used to built fb?" ,"python" , "french" , "javascript" , "php" , "none" ,4],
]

levels = [ 1000 , 2000 , 3000 , 5000 , 10000 , 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range (0 , len(questions)):
    question = questions[i]
    print(f" \n \n Question for Rs.{levels[i]}")
    print(f"a.{question[1]}  b.{question[2]}  c.{question[3]}  d.{question[4]} ")

    reply = int(input("Enter your answer between (1-4):"))

    if (reply==4):
        print(f"Correct answer, you have won Rs.{levels[i]}")

        if(i==4):
            money = 10000
        elif(i==9):
            money = 320000
        elif(i==14):
            money = 10000000
    else:
        print("wrong answer!")
        break


print(f"Your take money to home is {money}") 



