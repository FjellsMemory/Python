from sys import argv

script, mrormrs, user_name = argv
prompt = '$ '
script, mrormrs, user_name, occupation = argv
prompt = '-> '

print(f"Hi {mrormrs} {user_name}, I'm the {script} script.")
print(f"Hi {mrormrs} {occupation} {user_name}, I'm the {script} script.")
print(f"I'd like to ask you a few questions.")
print(f"Do you like me, {mrormrs} {user_name}?")
print(f"Do you like me, {mrormrs} {occupation} {user_name}?")
likes = input(prompt)

print(f"Where do you live {mrormrs} {user_name}?")
print(f"Where do you live {mrormrs} {occupation} {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, {mrormrs} {user_name}, so you said "{likes}" about liking me.
Alright, {mrormrs} {occupation} {user_name}, so you said "{likes}" about liking me.
You live in {lives}.  Not sure where that is.
And you have a {computer} computer.  Nice.
""")
