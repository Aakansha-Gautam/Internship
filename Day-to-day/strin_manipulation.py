#30th november: String manipulation

from ast import Raise


word="aakansha"

#string is immutable so any changes made on the string or operation performed will not affect the original string

s=word.upper()
print(s)

print("************************")

t=word.lower()
print(t)

print("****************************")

r=word.title()
print(r)

print("***********************")

i=word.count('a')
print(i)

print("*********************")

print(word)

strip_example="  __  AAkansha  __  "
print(strip_example.lstrip())

print(strip_example.rstrip(),".")

print("*",strip_example.strip(),"*")


print(strip_example)
print(word)


center_method=word.center((len(word))+4,"*")
print(center_method)

x="aakansha is my name OK Fine"
print(x.title()) # capitaloze the first character of every word present in the string
print(x.capitalize())

print(x.lower())
print(x.casefold())

print(x.split(" ")) # we can also set the maxsplit
print(x.split(" ",1))

# startswith() return boolean value
print(x.startswith('aakansha'))


#swapcase() method
# converts all uppercase to lowercase and vice versa
print(word.swapcase())

# zfill add '0' startinf from left side until it reach the desired length

print(word.zfill(15))

# trasform one word given in ascii to another
# use of dictionary to store the value

mydict = {65:  83, 97: 117}
txt = "Hello Aakansha!"
print(txt.translate(mydict))

print(x.rsplit(" ", 1))
print(x.rsplit(" ", 2))

info="Hi my name is aakansha\nI am practising string manipulation aakansha"
print(info.splitlines())

print(info.find('aakansha'))

print(info.rfind('aakansha'))

print(word.rjust(10,'*'))

print(info.rpartition('aakansha'))

print(info.endswith('aakansha'))

word1="the world is beautiful and is full of people, my name is aakansha , me is human"
w1=word1.replace("is","was")
w2=word1.replace("is","was",3)
print(w1)
print(w2)

print(word1.partition('is'))
