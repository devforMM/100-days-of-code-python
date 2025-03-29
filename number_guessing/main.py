import random
random_number=random.randint(1,100)

def check(n1,random):
    if random==n1:
        return "you are right"
    elif random<n1:
        return "too high"
    else:
        return "too low"
    
dificulty=input("choose a dificulty: ")
difficultys=["easy","hard"]
attempts=0
if dificulty=="easy":
    attempts=10
elif dificulty=="hard":
    attempts==5
print(f"you have already {attempts}")




while True:
    my_nbr=int(input("guess a number between 1 and 100: "))
    print(check(my_nbr,random_number))
    if check(my_nbr,random_number)=="you are right":
        break
    attempts-=1
    if attempts==0:
        print("you lost")
        break
    print(f"il vous reste {attempts}")
    
    


