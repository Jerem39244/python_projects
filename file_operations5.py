# Create a text file named Codingal.txt in write mode.
# Use a with statement and store the file object in a variable named file.
with open("Codingal.txt", "w") as file:
    file.write("Hi! I am Penguin and I am 1 yr old.")
    
file.close()
with open("Codingal.txt","r") as file:
    data = file.readlines()
    print("Words in the file are...")
    for line in data:
        word = line.split()
        print(word)

file.close()

# Inside the with block, write the text:
# "Hi! I am Penguin and I am 1 yr old."

# Do not manually close the file.
# The with statement will automatically close it.

# Open Codingal.txt again in read mode.
# Use a with statement and store the file object in a variable named file.

# Read all lines from the file and store them in a variable named data.

# Print the message:
# "Words in this file are...."

# Create a loop that processes each line in data.

# Inside the loop, split the current line into words.
# Store the resulting list in a variable named word.

# Print the word list.

# Do not manually close the file.
# The with statement will automatically close it.