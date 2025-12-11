import random
print("⚔️    Welcome to Dice Fight match  ⚔️")
print("⚠️   if Your Total Score Would Be Above Than 8 or Equal To 9 You Win But If You Cannot You Lose  ⚠️")
print("🎮  Press 1 to Start \n or \n Press 2 to Quit  😞")
a = int(input("Enter Your Decision : \n"))
if a == 1:
    print("Then Get Ready!!")
    print("🚀  Rolled  🚀")
    Dice_roll = random.randint(1,6)
    print(Dice_roll)
    print(" 🎮Press 10 To Start Next Match 🎮")
    b = int(input("Enter To Start Next match"))
    if b == 10:
        print ("⏭️  Next Match  ⏭️")
        print("ok!")
        print("🚀  Rolled  🚀")
        Dice_roll2 = random.randint(1,6)
        print(Dice_roll2)
    else:
        print("😠  You Have Entered Wrong Information  😠")
    print(" 🎮Press 20 To Start Final Match 🎮")
    d = int(input("Enter To Start Final match"))
    if d == 20:
        print("🎯  Final Match  🎯")
        print("🚀  Rolled  🚀")
        Dice_roll3 = random.randint(1,6)
        print(Dice_roll3)
        c = Dice_roll + Dice_roll2 + Dice_roll3
        print("Your Total Score is :",c)
        if c >= 12:
            print("🏆  You Won The  ⚔️  Dice Fight  ⚔️  🏆")
        elif c < 12:
            print("💔  You Lost The Dice Fight  💔")
            print("😊  No Worries Bette Luck Next Time  😊")
    else:
        print("😠  You Have Entered Wrong Information  😠")
            
elif a == 2:
    print("🕒  No Worries You Can Play Next Time  🕒")

else:
    print("😠  You Have Entered Wrong Information  😠")