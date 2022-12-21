# efficient
#less emmory less time


# def even(number):
#     l=[]
#     for i in number:
#         if i%2==0:
#             l.append(i)
#     return l
# print(even(range(1,11)))

# print("*************************************")

l=[i for i in range (0,13) if i%2==0]
print(l)

print("************************************")

l=[i**2 for i in range(1,11)]
print(l)

print("************************************")

l=[-i for i in range(1,11)]
print(l)

print("************************************")

name=['aakansha','saurya','pandey']
l=[i[0] for i in name ]
print(l)

print(*"*************************************")

def reverse(words):
    return([i[::-1] for i in words])
print(reverse(['aakansha','saurya']))

print("*****************************")

mix=['aakansha',True,[1,2,3],11,1.232,4]

l=[str(i) for i in mix if (type(i)==int or type(i)==float)]
print(l)


print("************************************")

# if else with list comprehension

nums=list(range(1,12))
l=[i*2 if (i%2==0) else -i for i in nums]
print(l)


print("*************************************")
# list inside list

nested=[[i for i in range(1,4)] for j in range(1,4)]
print(nested)