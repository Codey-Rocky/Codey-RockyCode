print("This Is For Sports Volunteers")
a = input("Enter Your Name")
b = input("Enter Your Age")
c = input("Enter Your Sports")
class person:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
p1 = person("Shaurya",11,"Badminton")
print("Let's Fill Your Data")
try:
    with open(c,'a') as f:
        f.write(f"Name Of Volunteer {a} And Age Of Volunteer {b}\n")
except:
    print("There Is An Error In Creating File")
finally:
    print("Your File Is Successfully Created!!")