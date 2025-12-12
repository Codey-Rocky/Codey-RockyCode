import random
print("Let's Play Stone Paer Scissors")
print("It Is A Two User Game")
while True:
    d = int(input("If You Want To Play With Computer Than Press 1 Or If You Want To Play Two User Than Press 2 And For Quit Press 3"))
    c = int(input("If You Want To Play Press 1 And If Not Then Press 2"))
    if d == 2:
        if c == 1:
            print("1 For Stone, 2 For Paper , 3 For Scissors")
            a = int(input("User 1 Enter Your Choice"))
            b = int(input("User 2 Enter Your Choice"))
            if (a >= 1 and a <= 3) and (b >= 1 and b <= 3):
                if (a is 1 and b is 2) or (a is 3 and b is 1) or (a is 2 and b is 3):
                    print("User 2 Won!!")
                elif(a is 1 and b is 3) or (a is 2 and b is 1) or (a is 3 and b is 2):
                    print("User 1 Won!!")
                else:
                    print("It Is A Tie Between The Two Users")
            else:
                print("You Have Entered Wrong Information")
        elif c == 2:
            print("Ok Bye Bye")
            break
        else:
            print("Wrong Information Has Been Entered")
    elif d == 1:
        print("Let's Play With Computer")
        print("1 For Stone, 2 For Paper , 3 For Scissors")
        e = int(input("Enter Your Choice"))
        f = random.randint(1,3)
        if (e is 1 and f is 3) or (e is 2 and f is 1) or (e is 3 and f is 2):
            print("You Won!!")
        elif (f is 1 and e is 3) or (f is 2 and e is 1) or (f is 3 and e is 2):
            print("Computer Won!!")
        else:
            print("Wrong Information Has Been Entered")
