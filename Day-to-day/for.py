s=0
num=int(input("Enter the number: "))
for i in range(1, num+1):
    s+=i
print (s)

print("**********************************")

name=input("Enter your name")
s=""
for i in range (len(name)):
    if name[i] not in s:
        s+=name[i]
        print(f"{name[i]}: {name.count(name[i])}")
        


for i in range(0,20):
    if(i==15):
        break
    elif i==2:
        continue
    else:
        print(i)
