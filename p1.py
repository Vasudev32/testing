# name = "Tony"
# age = 51
# is_genius = True#always remember in boolean True and False is written like this or T,F should be capital
# # print (name,age,is_genius)
# print("Hello "+name )
# print("I know u r a superhero. Can u plzz tell me ur superhero name:")
# superhero_name = input()
# # print(superhero_name)
# print("Printing 3 times")
# for i in range (3):
#     print(i,superhero_name)
# a = 2
# print(a)
# print("Value of a is",a)
# name = "Vasu"
# print(name.upper())

# Open the file in read mode
# text = open("sample.txt", "r")
text = "my name is vasu"

# Create an empty dictionary
d = dict()

# Loop through each line of the file
for line in text:
# 	# Remove the leading spaces and newline character
	line = line.strip()

# 	# Convert the characters in line to
# 	# lowercase to avoid case mismatch
	line = line.lower()

# 	# Split the line into words
	words = line.split(" ")
						

	# Iterate over each word in line
	for word in words:
		# Check if the word is already in dictionary
		if word in d:
			# Increment count of word by 1
			d[word] = d[word] + 1
		else:
			# Add the word to dictionary with count 1
			d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
	print(key, ":", d[key])

