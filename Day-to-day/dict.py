#dictionary has key value pair

info={'name':'Aakansha',"age":20,'Address':"boudha"}
print(type(info))

info_1=dict(name="aakansha",age=20,address='boudha')
print(type(info_1))

print(info['name'])

#word counter
def counter(word):
    count={}
    for i in word:
        number= word.count(i)
        count[i]=number
    return count
print(counter('Aakansha'))