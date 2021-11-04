from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    texts = question["text"]
    answers = question["answer"]
    new_q = Question(texts, answers)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    print(f"You've completed the quiz. Your final score is : {quiz.score}/{quiz.question_number}")
