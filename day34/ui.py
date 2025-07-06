from tkinter import *
import requests

User_answer = None

# ------------------------------------- data ---------------------------------------------------# 
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
        
response = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")
data = response.json()["results"]
Questions = [Question(question["question"], question["correct_answer"]) for question in data] 

# ------------------------------------- quiz brain ----------------------------------------------#
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        canevas.itemconfig(question, text=f"{self.question_number} - {self.current_question.text}")

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            
        
            
        score.config(text=f"{self.score}/{self.question_number}")
        
        

quiz = QuizBrain(Questions)
print(quiz.question_list)

def false_answer():
    global User_answer
    if quiz.still_has_questions():
        User_answer = "false"
        quiz.next_question()
        quiz.check_answer(User_answer)
    
def correct_answer():
    global User_answer
    if quiz.still_has_questions():
        User_answer = "true"
        quiz.next_question()
        quiz.check_answer(User_answer)

THEME_COLOR = "#375362"
screen = Tk()
screen.title("Quiz Game")
screen.minsize(500,650)
screen.config(padx=50, pady=100)
score = Label(text=" Current  Score : 0", font=("arial", 20, "bold"))
score.grid(row=0, column=1, columnspan=2)
true_image = PhotoImage(file="./day34/images/true.png")
false_image = PhotoImage(file="./day34/images/false.png")
canevas = Canvas(bg=THEME_COLOR, height=400, width=500)
canevas.grid(row=1, column=1, columnspan=2)
result=Label(text="",font=("Arial", 25))
result.grid(row=3,column=0,columnspan=2)
question = canevas.create_text(250, 200, text="", font=("Arial", 25), width=480,fill="white") 
false_button = Button(image=false_image, command=false_answer)
right_button = Button(image=true_image, command=correct_answer)
right_button.grid(row=2, column=1)
false_button.grid(row=2, column=2)
screen.mainloop()
