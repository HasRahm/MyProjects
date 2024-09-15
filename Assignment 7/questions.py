#Name: Hasin Shadab Rahman                                                             UID:U87513234
#Initialize a trivia question with the specified attributes.
#Parameters:
# - question (str): The trivia question.
# - answer1-4 (str): The possible answers to the question.
# - correct_answer (int): The number corresponding to the correct answer.
class Questions:
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correct_answer = correct_answer

    def __str__(self):
        return f"{self.question}\n1. {self.answer1}\n2. {self.answer2}\n3. {self.answer3}\n4. {self.answer4}"
