print("Do You Have Problem In Making Bank Account")
print("No Worries")
print("Now You Can Make It")
print("Yes You Heard It Right")
print("Which Company You Want To Make Your Account")
x = str(input("Enter Company"))
print("Ok Let's Make An Account In",x)
Bank_Acc = "Bank Account.txt"
with open("Bank_Acc",'x') as f:
    print("Created")
    f.close()
print("Now You Have A Bank Account")
print("Add,Withdraw,Review Money In Bank Account")
print("Enter 1 For Add \n or \n Enter 2 For Withdraw \n or \n Enter 3 For Review \n or \n Enter 4 For Close")
a = int(input("Enter Your Choice"))
i = 1
for i in range(i + 1):
    print("Enter 1 For Add \n or \n Enter 2 For Withdraw \n or \n Enter 3 For Review \n or \n Enter 4 For Close")
    a = int(input("Enter Your Choice"))
    if a == 1:
        b = int(input("Enter Bank Balance"))
        with open("Bank_Acc",'a') as f:
            f.write(f"Bank Balance : {b}")
            f.close()
    elif a == 2:
        c = int(input("Enter The Money You Want To Withdraw"))
        if c < f:
            print(f"{c} : Money WithDrawn From Bank Balance")
            print(f - c)
        elif c > f:
            print("You don't Have Enough Balance In Your Bank Account To Withdraw")
        else:
            print("Wrong Information")

    elif a == 3:
        d = str(input("Enter Yes or No"))
        if d == "Yes":
            print(f"Bank Balance Is:{f}")
        elif d == "No":
            print("Ok")

    elif a == 4:
        e = str(input("Do You Want To Close Yes or No"))
        if e == "Yes":
            print("Ok GoodBye")
        else:
            print("Ok")
            print("Enter 1 For Add \n or \n Enter 2 For Withdraw \n or \n Enter 3 For Review \n or \n Enter 4 For Close ")
