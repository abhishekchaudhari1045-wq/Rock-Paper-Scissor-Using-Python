import random

def game_win(user,computer):
    if user==computer:
        return None
    #Rock Vs Paper
    if user=="r" and computer =="p":
        return False

    if user=="p" and computer =="r":
            return True

    #Rock Vs Scissor
    if user=="r" and computer=="s":
        return True

    if user=="s" and computer=="r":
        return False
    

    #Paper Vs Scissor
    if user=="p" and computer=="s":
            return False
    
    if user=="s" and computer=="p":
            return True

rand_no=random.randint(1,3)

print("computer turn:Rock(r) Paper(p) Scissor(s)")

if rand_no==1:
    computer="r"
elif rand_no==2:
    computer="p"
else:
    computer="s"

user=input("Your turn:Rock(r) Paper(p) Scissor(s) : ").lower()

result=game_win(user,computer)

print(f"\nYou Choose:{user}")
print(f"\nComputer Choose:{computer}")

if result is None:
    print("its draw")

elif(result):
    print("you win!")

else:
    print("you lose!")

