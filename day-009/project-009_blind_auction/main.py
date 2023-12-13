import art
import os

# Welcome section
print(art.logo)
print("Welcome to the secret auction program.\n")


# Main code
def main():
    bids = {}

    get_bids = True
    while get_bids:
        new_bid = get_new_bid()
        bids[new_bid[0]] = new_bid[1]

        valid_input = False
        while not valid_input:
            get_another_bidder = input(
                "Are there any other bidders? Type 'yes' or 'no'.\n")

            if get_another_bidder.lower() == "yes":
                valid_input = True
                os.system('cls' if os.name == 'nt' else 'clear')
            elif get_another_bidder.lower() == "no":
                valid_input = True
                get_bids = False
            else:
                print("ERROR: Please enter only 'yes' or 'no'")

    work_out_winner(bids)


def get_new_bid():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    return [name, bid]


def work_out_winner(dict):
    highest_bidder = None
    highest_bid = 0
    for bid in dict:
        if dict[bid] > highest_bid:
            highest_bidder = bid
            highest_bid = dict[bid]

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")


if __name__ == '__main__':
    main()
