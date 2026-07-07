import os
with open("notes.txt", "w") as file:
    file.write("american revolution\n")
    file.write("civil war")
file.close()
with open("notes2.txt", "w") as file2:
   file2.write("English stuff:\n")
   file2.write("a, b, c, d, e, f, g")
file2.close()
with open("notes.txt", "r") as file:
    print(file.readlines())
with open("notes2.txt", "r") as file2:
    print(file2.readlines())
with open("notes.txt", "r") as file:    
    data = file.readlines()
    print("Words in the file are...")
    for line in data:
        word = line.split()
        print(word)
        word_count = len(word)
        print(f"Total words: {word_count}")
with open("notes2.txt", "r") as file2:    
    data = file2.readlines()
    print("Words in the file 2 are...")
    for line in data:
        word = line.split()
        print(word)
        word_count = len(word)
        print(f"Total words: {word_count}")


file.close()
file2.close()
if __name__ == '__main__':
    
    

    while(True):
        print("What do u want to do")
        print("1. check for merged files")
        print("2. merge files")
        print("3. delete files")
        user_choice = input()
        if user_choice not in ['1','2','3']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)
        
        if user_choice == 1:
            print("Checking for merged files...")
            if os.path.exists("study_guide.txt"):
                print("item found")
            else:
                print("Item not found")
        
        elif user_choice == 2:
           print("Checking if a merged file already exists...")
           if os.path.exists('study_guide.txt'):
               print("file already exists")
           else:
                print("Merging files...")
                # create/overwrite merged file
                with open('study_guide.txt', 'w') as out:
                    if os.path.exists('notes.txt'):
                         with open('notes.txt', 'r') as n1:
                             out.write(n1.read())
                             out.write("\n")
                    if os.path.exists('notes2.txt'):
                        with open('notes2.txt', 'r') as n2:
                            out.write(n2.read())
                print('Merged into study_guide.txt')
               
               
               

        elif user_choice == 3:
            user_choice1 = input("What files do you want to remove: study_guide.txt,notes.txt,notes2.txt ")
            if user_choice1 == "study_guide.txt":
                if os.path.exists("study_guide.txt"):
                    print("Deleting file now...")
                    os.remove("study_guide.txt")
                else:
                    print("file does not exist")
            elif user_choice1 == "notes.txt":
                if os.path.exists("notes.txt"):
                    print("Deleting file now...")
                    os.remove("notes.txt")
                else:
                    print("file does not exist")
            elif user_choice1 == "notes2.txt":
                if os.path.exists("notes2.txt"):
                    print("Deleting file now...")
                    os.remove("notes2.txt")
                else:
                    print("file does not exist")




        else:
            print("Not a valid option")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                print("Good luck on your test, Bye")
                exit()

            elif user_choice2 == "c":
                continue
