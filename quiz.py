questions = [
    
    {"question":"🟩 What does UK stand for?",
     "options":["U know","United Kingdom", "Ulala", "Ur Kind"],
     "correct":"United Kingdom"
     },
    {"question":"🟩 What does IDK stand for?",
     "options":["I do know","I don't know", "In Door Kings", "If da kids"],
     "correct":"I don't know"
     },
    {"question":"🟨 What does WSG stand for?",
     "options":["What's good","Woah selective guy", "Well so good", "What stands go"],
     "correct":"What's good"
     },
    ]

def quiztime():
    score = 0

    print("QuizTime!")

    for q, diction in enumerate(questions):
        print("Question ",q+1,": ",diction["question"])

        for _ in range(len(diction["options"])):
            print("Option, ",_+1,":",diction["options"][_])
        a = input("Answer the number of the qeustion: ")

        if a.isdigit() and 1<= int(a) <= 4:
            if diction["correct"] == diction["options"][int(a)-1]:
                print("yup, lets go to the next question!")
                score += 1
            else:
                print("Wrong. Better luck next time!")
        else:
            print("Numbers only.")

    print("Score: ",score,"/",len(questions))

quiztime()
