from question_model import Question
from data import question_data


def main():
    print()
    get_question_bank()


def get_question_bank():
    question_bank = []
    for data in question_data:
        question_bank.append(Question(data["text"], data["answer"]))
    return question_bank


if __name__ == "__main__":
    main()
