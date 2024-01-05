from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
    question_bank = get_question_bank()
    quiz = QuizBrain(question_bank)
    still_has_questions = quiz.still_has_questions()
    while still_has_questions:
        quiz.next_question()
        quiz.handle_user_guess()


def get_question_bank():
    question_bank = []
    for data in question_data:
        question_bank.append(Question(data["text"], data["answer"]))
    return question_bank


if __name__ == "__main__":
    main()
