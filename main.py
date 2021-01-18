import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index, row) in data.iterrows()}
def ok():
    word = input("Enter a WRLD ").upper()
    try:
        output = [dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only words")
        ok()
    else:
        print(output)
ok()