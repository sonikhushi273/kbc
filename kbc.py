questions = [["Which language was used to create fb?" , "python" , "javascript", "French" , "HTML & CSS", 1],
             ['The International Literacy Day is observed on', 'Nov 28', 'May 2', 'Sep 22', 'Sep 8', 4],
             ['Bahubali festival is related to', 'Islam', 'Jainism', 'Hinduism', 'Buddhism', 2]]
             
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 250000,500000,10000000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs.{levels[i]}")
    print(f"{question[0]}")
    print(f"1.{question[1]}        2.{question[2]}")
    print(f"3.{question[3]}        4.{question[4]}")
    reply = int (input("Enter your answer(1-4) or 0 to quit:\n"))
    if (reply == 0) and (i == 0):
        money = 0
        print('Aayein hi kyun the ?')
        break
    if (reply == 0) and (i != 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):
        print(f"Correct answer, you have won {levels[i]}")
        money = levels[i]
    else:
        print ("Wrong answer oops!, Chalo niklo")
        money = levels[i-1]
        break
        
print(f"You have won total of {money} amount.")
