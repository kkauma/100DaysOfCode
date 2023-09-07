# Dictionaries (key -> value)

programming_dictionary = {
    "Bug": "An error in a program that presents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

# print(programming_dictionary["Function"])


# Adding new items to a dictionary
programming_dictionary["Class"] = "A blueprint for designing a real life object."
# print(programming_dictionary)

# Create an empty dictionary
empty_dict = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A mistake in a codebase that doesn't allow the code to run or compile properly."
# print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])