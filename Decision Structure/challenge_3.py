# Make a program that checks if a letter typed is "F" or "M".
# Write Female if the letter is F or Male if the letter is M if neither of them write Invalid Gender.

def get_gender():
    while True:
        genre = str(input('You are male or female? Insert W or M: ')).upper()

        if genre in ('W', 'M'):
            if genre == "W":
                return "Woman"
            else:
                return "Man"
        else:
            print('Invalid Gender. Try again. ')
            continue


print(get_gender())
