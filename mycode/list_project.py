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
strlist = [x.lower() for x in strlist] # List Comprehension!!!
strlist.sort()
strlist = [x.upper() if (strlist.index(x)%2 == 0) else x.lower() for x in strlist]
print(strlist)
print("Nice one.  Here's the list alphabetical.")
print("Continue to enter new terms.")
print("Watch how they insert themselves into their rightful place.")
input3 = input("Go head, son (when finished enter 'Done'):  ")
while input3 != "Done":
    strlist.append(input3.lower())
    strlist = [elem.lower() for elem in strlist]
    strlist.sort()
    strlist = [x.upper() if (strlist.index(x)%2 == 0) else x.lower(x) for x in strlist]
    print(strlist)
    input3 = input("Keep going (when finished enter 'Done'):  ")
print("Great job, Mandingo!")

#  adding extra text here just to test .git push to GitHub
