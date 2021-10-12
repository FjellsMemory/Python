from sys import argv

script, from_file, to_file = argv

in_file = open(from_file)
in_data = in_file.read()
print(type(in_data))

out_file = open(to_file, "w")

out_file.write(in_data)

in_file.close()
out_file.close()
