import random
import art

############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

DECK = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def main():
    user_hand = []
    computer_hand = []
    playing = True
    while playing:
        for i in range(2):
            user_hand.append(draw_card())
            computer_hand.append(draw_card())

        user_score = get_score(user_hand)
        computer_score = get_score(computer_hand)

        print(f"Your cards: {user_hand}")

        playing = False  # For testing


def draw_card():
    return random.choice(DECK)


def get_score(hand):
    score = sum(hand)
    if score > 21:
        if 11 in hand:
            hand.pop(hand.index(11))
            hand.append(1)
            score = sum(hand)
    return score


if __name__ == "__main__":
    print(art.logo)
    main()
