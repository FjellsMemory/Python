print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot descern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("_______________")
print(poem)
print("_______________")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another wy to format a string
print("with a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

# all this makes sense - but i never saw that last move, where homie packed
# three variables into one with formula = secret_formula(start_point)
# this is a boss move and actually makes formula a tuple, and after that
# *forumla unpacks the tuple and feeds the contents like a generator to 
# .format({} {} {})
