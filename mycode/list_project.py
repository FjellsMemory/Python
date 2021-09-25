# - ask for inputs to construct list of strings
# - sort list alphabetically and print
# - ask for new inputs until "done" is entered, each time adding new inputs
# -   to list and reprinting with new entry in its rightful place

input1 = input("Enter a series of words (when finished enter 'Done'):  ")
strlist = [input1]
input2 = input("Keep going:  ")
while input2 != "Done":
    strlist.append(input2)
    input2 = input("Keep going:  ")
low_strlist = [x.lower() for x in strlist] # use of LIST COMPREHENSION!!!
strlist = low_strlist
strlist.sort()
print(strlist)
print("Nice one.  Here's the list alphabetical.")
print("Continue to enter new terms.")
print("Watch how they insert themselves into their alphabetical place.")
input3 = input("Go head, son (when finished enter 'Done'):  ")
while input3 != "Done":
    elem = input3.lower()
    strlist.append(elem)
    strlist.sort()
    print(strlist)
    input3 = input("Keep going (when finished enter 'Done'):  ")
print("Great job, Mandingo!")
