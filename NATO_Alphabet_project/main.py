import pandas 

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter : row.code for (index,row) in nato_data.iterrows()}
Code = input("Enter the Word : ").upper()

Code_list =[nato_dict[letters] for letters in Code]
print(Code_list)


