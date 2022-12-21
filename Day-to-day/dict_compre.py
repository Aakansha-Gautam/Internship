
square={i:i**2 for i in range(1,10)}
print(square)

print("****************************")

name="Aakansha"
word_count={i:name.count(i) for i in name }
print(word_count)


print("*****************************************")

# dict comprehension with if else

new={i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(new)
