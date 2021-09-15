
# str1 = "Yo boi this is the coolest thing ever."
# strlist = str1.split(" ")
# print(strlist)
# str1 = " ".join(i for i in strlist)
# print(str1)
#
# str2 = "hello"
# choppedlist = list("hello")
# print(choppedlist)
#
integer1 = 123456
intlist = list(str(123456))
print(intlist)
realintlist = list(int(i)for i in str(integer1))
print(realintlist)
#
# mydict = {"bob": 1, "mary": 5, "sigmund": 76}
# keyslist = list(mydict.keys())
# valueslist = list(mydict.values())
# unclear = mydict.values()
# print(unclear)
# print(type(unclear))
#
# print(keyslist)
# print(valueslist)
# print(mydict)
#
# mylist = [1, 2, 3, 4]
# mylist.insert(2, True)
# print(mylist)
# mystr = "funky"
#
# mylist.insert(mylist.index(4)+1, "sparrow") # genius
# print(mylist)

mylist = [1, 2, 3, 4]
mylist.sort(reverse = True)
print(mylist)
mylist.reverse()
print(mylist)
print(len("str1"))

mystrlist = ["james", "jamie", "homie", "home biscuit"]
print(max(mystrlist))
mystrlist.sort()
print(mystrlist)
