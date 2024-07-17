from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question = i["question"]
    answer = i["correct_answer"]
    new_q = Question(text=question, answer=answer)
    question_bank.append(new_q)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score was: {quiz.score}/{quiz.question_number}.")
