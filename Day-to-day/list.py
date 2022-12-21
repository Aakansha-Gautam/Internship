#basic list functions

l=[]
l=list(range(0,11))
print(l)

l[0]="add"
print(l)

#adding into list 

l.append("append")
print(l)

l2=[22,11,44,33,55]

l.extend(l2)
print(l)

l.insert(2,"insert")
print(l)

l.pop()
print(l)

del l[2]
print(l)

l.remove("add")
print(l)
l.remove("append")
l.sort()
print(l)

print(l.count(11))

l.clear()
print(l)


print(l)

fruits=['apple','kiwi']
print((",".join(fruits)))

f="1,2,3"
print((",".split(f)))

print(l.index(11))