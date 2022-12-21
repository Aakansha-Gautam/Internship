# while loop
a=1
sum=0
while(a<=10):
    sum+=a
    a+=1
print(sum)


print("**************************************")

number=input("ENter more than one digit: ")
i=0
total=0
while(i<len(number)):
    total+=int(number[i])
    i+=1
print(total)


print("**************************************")

name=input("Enter you full name: ")
i=0
l=""
while(i<len(name)):
    if (name[i] not in l):
        l+=name[i]
        count=name.count(name[i])
        print(f"{name[i]}: {count}")
    i+=1
