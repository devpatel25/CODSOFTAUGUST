# Task 5- Quiz Game
import random

# python Quiz
def python_mcq():
    mcq={"What is the maximum length of a Python identifier?": ['No Fixed length is specified',32,12,10],
        "How is a code block indicated in Python?": ['Indentation','Brackets','Key','None of the Above'],
        "Which of the following concepts is not a part of Python?": ["Pointers","Loops","Dynamic Typing","All of the Above."],
        "Which of the following statements are used in Exception Handling in Python?": ["All of the Above","Try","except","finally"],
        "Which of the following types of loops are not supported in Python?":["do-while","while","for","Non of the above"]
        }
    return mcq

# General Knowledge Quiz
def generalknowledge_mcq():
    mcq={
        "Grand Central Terminal, Park Avenue, New York is the world's":["largest railway station","highest railway station","longest railway station","None of the above"],
        "Entomology is the science that studies":["Insects","Behavior of human beings","The origin and history of technical and scientific terms","The formation of rocks"],
        "Garampani sanctuary is located at": ["Diphu, Assam","Junagarh, Gujarat","Kohima, Nagaland","Gangtok, Sikkim"],
        "For which of the following disciplines is Nobel Prize awarded?": ["All of the above","Physics and Chemistry","Physiology or Medicine","Literature, Peace and Economics"],
        "When is the World's Diabetes Day?": ["14th November","11th December","15th October","1st July"]
    }
    return mcq

# Science quiz
def science_mcq():
    # write 5 mcqs questions related to science with its answers and options.
    mcq = {

        "What is the process by which plants make food?": ["Photosynthesis","Cellular respiration","Transpiration","Nitrogen fixation"],
        "Which of the following is a renewable resource?" : ["Solar energy","Oil","Natural gas","Coal"],
        "What is the largest organ in the human body?": ["Skin","Heart","Lungs","Brain"],
        "Which of the following is a greenhouse gas?" :["Carbon dioxide","Oxygen","Nitrogen","Argon"],
        "What is the theory that states that the universe began as a single point and has been expanding ever since?" : ["Big Bang theory","Steady state theory","Oscillating universe theory","Multiverse theory"]
    }
    return mcq





# shuffle mcq
def shuffle_mcq(mcq):
    mcq_list=list(mcq.items())
    random.shuffle(mcq_list)
    shuffled_mcq=dict(mcq_list)
    return shuffled_mcq



# quiz
def quiz(shuffled_mcq):
    score=0
    labels=["A","B","C","D"]
    for num,(question,choices) in enumerate(shuffled_mcq.items(),start=1):
        print(f"{num}.) {question}")
        correct_ans=choices[0]
        random.shuffle(choices)
        labeled_choices=dict(zip(labels,choices))
        for label,choice in labeled_choices.items():
            print(f"{label}) {choice}")
        answer_label=input("Answer: ")
        answer=labeled_choices.get(answer_label)
        if (answer==correct_ans):
            score+=1
            print("Correct!")
        else:
            print("Incorrect!")
            print(f"Correct answer is {correct_ans} and not {answer}")
    print("\n")
    print("************************************")
    print("\tSCORES")
    print(f"You scored {score} out of {len(shuffled_mcq)}")
    print(f"Percentage: {score/len(shuffled_mcq)*100}%")
    print("\n***********************************\n")
        

# main
print("\n\n\t*WELCOME TO THE QUIZ*")
print("***********************************")
while True:
    print("\tA)Python Quiz")
    print("\tB)General Knowledge Quiz")
    print("\tC)Science Quiz")
    print("\tD)Exit")
    print("\n***********************************")

    choice = input('Please enter your Choice:')
    match choice:
        case "A":
            print("\n************************************")
            print("\tPYHTON QUIZ")
            print("************************************\n")
            shuffled_mcq=shuffle_mcq(python_mcq())
            quiz(shuffled_mcq)
        case 'B':
            print("\n************************************")
            print("\tGENERAL KNOWLEDGE QUIZ")
            print("************************************\n")
            shuffled_mcq=shuffle_mcq(generalknowledge_mcq())
            quiz(shuffled_mcq)
        case 'C':
            print("\n************************************")
            print("\tSCIENCE QUIZ")
            print("************************************\n")
            shuffled_mcq=shuffle_mcq(science_mcq())
            quiz(shuffled_mcq)
        case "D":
            print("\n")
            print("Thank You! Have a nice day ahead.")
            print("************************************")
            break
            
