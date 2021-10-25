from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank =[]

for data in question_data:
  d_text = data['question']
  d_answer = data['correct_answer']
  user_q = Question(d_text,d_answer)
  question_bank.append(user_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
  
  quiz.next_question()
print("you completed the quiz")
print(f"your final score is {quiz.score}/{quiz.question_number} ")  
  
    
  
    