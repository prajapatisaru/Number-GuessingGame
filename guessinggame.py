import random
winning_num=random.randint(1,100)
guess=1
user=int(input("guess the number between 1 and 100:"))
game_over =False
while not game_over:
    if user==winning_num:
        print(f"you win and u guessed this number in {guess} time")
        game_over=True
    else:
        if user>winning_num:
                print("too large.")
        else:
            print("Too small.")
        guess+=1
        user=int(input("guess again: "))

    
        


