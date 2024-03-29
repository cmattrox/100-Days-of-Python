import requests
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

res = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
res.raise_for_status()
data = res.json()

question_bank = []
for question in data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_interface = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
