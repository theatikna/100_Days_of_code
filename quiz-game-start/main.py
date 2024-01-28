from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    ans = question["answer"]
    new = Question(text, ans)
    question_bank.append(new)

# Create a QuizBrain instance
quiz = QuizBrain(question_bank)

# Continue asking questions while there are still questions left
while quiz.still_has_question():
    quiz.next_question()

print("You Have Completed the Quiz")
print(f"Your Total Score {quiz.score}/{quiz.number}")
