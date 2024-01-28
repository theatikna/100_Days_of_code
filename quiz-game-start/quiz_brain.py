class QuizBrain:
    def __init__(self, question_list):
        self.number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.number < len(self.question_list)

    def next_question(self):
        if self.still_has_question():
            current_question = self.question_list[self.number]
            user_response = input(f"Q{self.number + 1}: {current_question.text} (True/False): ")
            self.check_answer(user_response, current_question.answer)
            self.number += 1
        else:
            print("You have completed the quiz.")

    def check_answer(self, user_response, correct_answer):
        if user_response.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1

        else:
            print(f"Wrong. The correct answer is {correct_answer}.")
        print(f"Your Score {self.score} / {self.number+1}")