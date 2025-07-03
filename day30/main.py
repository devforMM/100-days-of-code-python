import pandas


data=pandas.read_csv("./day26/nato.csv")

dictionnaire={ row.letter:row.code for (index,row) in data.iterrows()}

print(dictionnaire)

while True:
 try:
    word=input("enter a word: ").upper()
    output_list=[dictionnaire[letter] for letter in word]
    print(output_list)
 except KeyError:
     print('sorry , only alphabet letters please ')