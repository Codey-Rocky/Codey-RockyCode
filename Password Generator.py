import random
print("🌈 Welcome To Password Generator 🌈")
print("😭 Having Problem To Choose A Password for Devices 😭")
print("🌞 No Worries, I will Help You 🌞")

name =  str(input("Can I Get Your Name Sir Or Madam \n"))
Words = ("QWERTYUIOPASDFGHJKLZXCVBNM")
Numbers = ("1234567890")

a = Words + Numbers

Digits = int(input("🌲 How Much Long You Have To Make The Password 🌲 \n ➡️ "))
print("🛸 Ok The Password Will Come Vertically At The Right Side 🛸")
for i in range(Digits):
    b = random.choice(a)

    print("👀 The Wait Is Over, Your Password Is 👀:|",b,"|")

print("👍 Give Us Ratings [Bad,Good,Very Good,Excellent] 👎 ")

S = str(input("🎈 Enter Your Ratings Towards Us 🎈: \n"))

if S == "Excellent":
    print("🥳 Thank You,",name,"Made My Day 🥳")

elif S == "Very Good":
    print("😁 Thank You Very Much 😁",name)

elif S == "Good":
    print("😊 Thank's For Your Ratings 😊",name)

elif S == "Bad":
    print("🥺 No Worries,Thanks For Your Help 🥺",name)

else:
    print("😠 You Have Entered Wrong Information 😠",name)
