from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
    question_bank = get_question_bank()
    quiz = QuizBrain(question_bank)
    still_has_questions = quiz.still_has_questions()
    while still_has_questions:
        question = quiz.next_question()
        guess = quiz.get_user_guess(question)
        quiz.check_answer(guess)
        quiz.increment_question_number()
        still_has_questions = quiz.still_has_questions()

    print("You've complete the quiz")
    print(f"Your final score was: {quiz.get_score()}/{len(question_bank)}")


def get_question_bank():
    question_bank = []
    for data in question_data:
        question_bank.append(Question(data["text"], data["answer"]))
    return question_bank


if __name__ == "__main__":
    main()
