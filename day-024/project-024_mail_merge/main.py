# TODO: Create a letter using starting_letter.txt 
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def main():
    for name in open("day-024/project-024_mail_merge/Input/Names/invited_names.txt").readlines():
        stripped_name = name.strip()
        letter = open("day-024/project-024_mail_merge/Input/Letters/starting_letter.txt").read()
        new_letter = letter.replace("[name]", stripped_name)
        with open(f"day-024/project-024_mail_merge/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as finished_letter:
            finished_letter.write(new_letter)


if __name__ == "__main__":
    main()
