import getpass, sys

questions = 5
correct = 0

def question_and_answer(prompt, answer):
    print("Question: " + prompt)
    msg = input()
    print("Answer: " + msg)

    if answer == msg:
        print("Correct Answer")
        global correct
        correct+=1
    else:
        print ("Incorrect Answer")
 
question_and_answer("What team does Lebron James play for?", "Lakers")
question_and_answer("What team does Kevin Durant play for?", "Nets")
question_and_answer("What team does Stephen Curry play for?", "Warriors")
question_and_answer("Who won the 2022 NBA Championship?", "Warriors")
question_and_answer("Who is the G.O.A.T?", "Michael Jordan")


print(correct, "Answers correct")