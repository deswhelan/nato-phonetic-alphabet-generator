#TODO: stretch - refactor to use pandas to read csv file, iterrows

with open("nato_phonetic_alphabet.csv") as nato_phonetic_alphabet_file:
    nato_phonetic_alphabet = nato_phonetic_alphabet_file.read().split("\n")

nato_phonetic_alphabet.pop(0)
nato_phonetic_alphabet_dict = {item.split(",")[0]:item.split(",")[1] for item in nato_phonetic_alphabet}

word_to_code = input("What word would you like to spell using the NATO phonetic alphabet?\n")

input_is_validated = False

while not input_is_validated:
    try:
        coded_word = [nato_phonetic_alphabet_dict[char.upper()] for char in word_to_code]
        input_is_validated = True
    except KeyError:
        print("Oops! Only letter are allowed!")
        word_to_code = input("What word would you like to spell using the NATO phonetic alphabet?\n")
    else:
        print(coded_word)


