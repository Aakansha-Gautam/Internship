num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
def gret(num1,num2):
    if(num1>num2):
        return ("number 1 is greater")
    return("number 2 is greater")
print(gret(num1,num2))



print("*********************************")


def pali(value):
    return value==value[::-1]
print(pali("bye"))
print(pali("eye"))

print("*************************************")

def fibo(num):
    a=0
    b=1
    if (num==1):
        print(a)
    elif(num==2):
        print(a,b)
    else:
        print(a,b, end =" ")
        for i in range(num-2):
            c=a+b
            a=b
            b=c
            print(b, end=" ")
num=int(input("ENter the number for fibonacci: "))
fibo(num)