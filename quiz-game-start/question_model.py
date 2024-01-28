class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer
ques = Question("Hey","False")
print(ques.text)