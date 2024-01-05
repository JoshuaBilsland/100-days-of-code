class QuizBrain:
    def __init__(self, question_list):
        self.__question_number = 0
        self.__question_list = question_list

    def next_question(self):
        current_question = self.__question_list[self.__question_number]
        return current_question

    def handle_user_guess(self, question):
        user_guess = input(
            f"Q.{self.__question_number+1}: {question["text"]} (True/False): ")
