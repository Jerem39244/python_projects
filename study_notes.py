sample_content = """1. IMPORTANT: Buy groceries.
2. Review Python notes.
3. IMPORTANT: Pay bills.
"""

with open("notes.txt", "w") as file:
    file.write(sample_content)

with open("notes.txt", "r") as file:
    print(file.read(15))
    print("-" * 20)

with open("notes.txt", "r") as file:
    print(file.readlines())
    print("-" * 20)

with open("notes.txt", "r") as src, open("important.txt", "w") as dest:
    for line in src:
        if "IMPORTANT" in line:
            print(line.strip())
            dest.write(line)
