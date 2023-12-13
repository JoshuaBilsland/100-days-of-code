import art

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
            elif get_another_bidder.lower() == "no":
                valid_input = True
                get_bids = False
            else:
                print("ERROR: Please enter only 'yes' or 'no'")


def get_new_bid():
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    return [name, bid]


if __name__ == '__main__':
    main()
