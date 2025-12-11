import random
print("🎮 Hello Guys Let's Play A Game Name Number Guessing Game 🎮")
print("🎨 In It You Have To Guess The Number Between 1 To 10 Which Computer Choose On The Basis Of Hints 🎨")
print("💭 Can you Enter Your Name For Playing It or Starting It 💭")
a = str(input(" 👩‍🏫 Enter Your Name 👩‍🏫 \n"))
print("🕹️  Ok",a,"You Can Play Now  🕹️")
print("🎾 My Last Question Is That",a,"If You Want To\nPlay Then Press 1 \n If You Don't Want To Play Then Press 2 🎾")
print("👨‍🏫  As The All Game Is About Mood , Time And Concentration 👨‍🏫")
b = int(input(" 👩‍🏫 Enter Mood at The Basis Of 1 and 2 \n"))
if b == 1:
    print("Ok Let's Play The Game")
    c = random.randint(1,10)
    if c == 1:
        print("💡 Hint = (It Is Neither Prime Nor Composite) 💡")
    elif c == 2:
        print("💡 Hint = (It Is Only Even Prime Number In Number Line) 💡")
    elif c == 3:
        print("💡 Hint = (It's Shape Is Half Of The Shape Of 8) 💡")
    elif c == 4: 
        print("💡 Hint = (It's The First Friend Of 2) 💡")
    elif c == 5:
        print("💡 Hint = (It's The Number Of Fingers On One Hand) 💡")
    elif c == 6:
        print("💡 Hint = (Hrithik Roshan Has How Many Fingers In His One Hand) 💡")
    elif c == 7:
        print("💡 Hint = (Cristiano Ronaldo Siuuuu) 💡")
    elif c == 8:
        print("💡 Hint = (It Is A Tower Of 2 Balls) 💡")
    elif c == 9:
        print("💡 Hint = (When We +1 In It Then It Completes 10 Marks) 💡")
    elif c == 10:
        print("💡 Hint = (Mom Appreciates When These marks Come \n In Small Tests of Any Subject) 💡")
    else :
        print("👻 Not Exsists in The Game 👻")
    d = int(input("Enter Your Answer \n"))
    if d == c:
        print("🥇 You Won The Game 🥇")
    else:
        print("😞 Better Luck Next Time 😞")        