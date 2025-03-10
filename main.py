import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dataframe = pandas.DataFrame(data)

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a Word\n").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)