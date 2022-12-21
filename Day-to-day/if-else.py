name=input("Enter your name: ")
if name=="Aakansha":
    print("Hi aakansha I missed you")
else:
    print("Who are you")


print("*******************************************")



import random
guess=int(input("Enter the number: "))
number=random.randint(0,100)
if(guess==number):
    print("Correct")
else:
    if(guess>number):
        print("high")
    else:
        print("low")
print(f"Answer: {number}")

print("*******************************************")

age=int(input("ENter your age: "))
if (age>=0 and age<=3):
    print('Free')
elif(age>=4 and age<=10):
    print('150')
elif(age>=11 and age<=60):
    print('250')
else:
    print('200')