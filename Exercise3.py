# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

#pseudocode


# Step 1: Accept input string from a user
# Step 2: Print the original string

# Step 3: Get the length of the string


# Step 4: Iterate over each character of the string
# Start: 0 to start with the first character
# Stop: size because index starts with 0
# Step: 2 to get the characters present at even index like 0, 2, 4
# Step 5: Print characters at even indices
# Step 6: Accept input string from a user  
# Step 7: Print the original string
# Step 8: Using list slicing
# Step 9: Iterate over the list and pick only even index chars
# Step 10: Print characters at even indices



# ------------------------------actual code----------------------------------------------------------
# Step 1: Accept input string from a user
word = input('Enter a word: ')
# Step 2: Print the original string
print("Original String:", word)

# Step 3: Get the length of the string
size = len(word)


# Step 4: Iterate over each character of the string
# Start: 0 to start with the first character
# Stop: size because index starts with 0
# Step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size, 2):
    # Step 5: Print characters at even indices
    print("index[", i, "]", word[i])
    
