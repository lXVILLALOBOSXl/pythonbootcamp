from util import get


class QuizBrain:
    def __init__(self, question_list):
        self.u_score = 0
        self.q_number = 0
        self.q_list = question_list

    def next_question(self):
        user_answer = get(F"Q.{self.q_number + 1}: {self.q_list[self.q_number].text} (True/False)?: ", str).lower()
        self.check_answer(user_answer, self.q_list[self.q_number])
        self.q_number += 1

    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def check_answer(self, answer, question):
        if answer == question.answer.lower():
            print("You got it right!")
            self.u_score += 1
        else:
            print("That's wrong.")
        print(F"The correct answer was: {question.answer}.")
        print(F"Your current score is: {self.u_score}/{self.q_number+1}\n")
