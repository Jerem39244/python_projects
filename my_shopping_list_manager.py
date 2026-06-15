filename = "shopping_list.txt"

print("--- Step 1 & 2: Creating file and writing initial list ---")
initial_items = ["Apples\n", "Milk\n", "Bread\n", "Eggs\n"]

with open(filename, "w") as file:
    file.writelines(initial_items)
print(f"Initial shopping list written to '{filename}'.\n")


print("--- Step 3: Reading the complete file ---")
with open(filename, "r") as file:
    content = file.read()
    print(content)


print("--- Step 4: Appending new items ---")
new_items = ["Butter\n", "Coffee\n"]

with open(filename, "a") as file:
    file.writelines(new_items)
print("New items appended successfully.\n")


print("--- Step 5: Reading the updated file line by line ---")
with open(filename, "r") as file:
    line_number = 1
    for line in file:
        print(f"Item {line_number}: {line.strip()}")
        line_number += 1
