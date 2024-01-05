class QuizBrain:
    def __init__(self, question_list):
        self.__score = 0
        self.__question_number = 0
        self.__question_list = question_list

    def get_score(self):
        return self.__score

    def increment_question_number(self):
        self.__question_number += 1

    def still_has_questions(self):
        return self.__question_number != len(self.__question_list)

    def next_question(self):
        current_question = self.__question_list[self.__question_number]
        return current_question

    def get_user_guess(self, question):
        return input(
            f"Q.{self.__question_number+1}: {question.get_text()} (True/False): ")

    def check_answer(self, user_guess):
        if (user_guess.lower() ==
                self.__question_list[self.__question_number].get_answer()
                .lower()):
            print("You got it right!")
            self.__score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: "
              f"{self.__question_list[self.__question_number].get_answer().lower()}")

        print(f"Your current score is: {self.__score}/{self.__question_number + 1}")
        print()
