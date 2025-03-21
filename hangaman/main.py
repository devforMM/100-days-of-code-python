import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

randow_word=random.choice(word_list)
print(randow_word)

lives=6
blanks=[]
for _ in range(len(randow_word)):
    blanks.append("_")

print(logo)


while True:
 guess=input("guess a letter:").lower()
 if guess in blanks:
    print("you have alread guessed the letter")


 if guess not in randow_word:
    print(stages[lives])
    lives-=1

 for i  in  range(len(randow_word)):
    if randow_word[i]==guess:
        blanks[i]=randow_word[i]
    
        
 print(f"{' '.join(blanks)}")

 if blanks.count("_")==0 :
    print("you win")
    break
 if lives==-1:
    print("you lose")
    break
 




