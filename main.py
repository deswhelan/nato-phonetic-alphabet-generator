with open("nato_phonetic_alphabet.csv") as nato_phonetic_alphabet_file:
    nato_phonetic_alphabet = nato_phonetic_alphabet_file.read().split("\n")

nato_phonetic_alphabet.pop(0)
nato_phonetic_alphabet_dict = {item.split(",")[0]:item.split(",")[1] for item in nato_phonetic_alphabet}

word_to_code = input("What word would you like to spell using the NATO phonetic alphabet?\n")

coded_word = [nato_phonetic_alphabet_dict[char.upper()] for char in word_to_code]

print(coded_word)
