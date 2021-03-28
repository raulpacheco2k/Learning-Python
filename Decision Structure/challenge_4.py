# Make a Program that checks if a letter is a vowel or consonant.

def vowel_or_consonant():
    while True:
        letter = str(input("Enter a letter: ")).upper()

        if validates_if_it_is_a_letter(letter):
            if letter in ("A", "E", "I", "O", "U"):
                print("The letter is a vowel.")
            else:
                print("The letter is a consonant.")
            break
        else:
            continue


def validates_if_it_is_a_letter(letter):
    if len(letter) > 1:
        print("digite somente uma letra")
    elif letter in "1234567890":
        print("digite uma letra.")
    else:
        return True


vowel_or_consonant()