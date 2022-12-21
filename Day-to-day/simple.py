import random
g=int(input("ENter the number from 0 to 100: "))
a=random.randint(0,100)
count=1
over=False
while not over:
    if(g==a):
        print(f"you win, and you gusses this number in {count} times")
        over=True
    else:
        if(g>a):
            print("high")
        else:
            print("low")
        count+=1
        g=int(input("ENter the number from 0 to 100: "))