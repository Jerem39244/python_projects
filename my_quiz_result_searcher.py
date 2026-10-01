quiz_results = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Emma": 88,
    "Frank": 76,
    "Grace": 95,
    "Henry": 83,
    "Ivy": 89,
    "Jack": 91
}


def direct_access(results, name):
    return results.get(name)


def linear_search(results, target_score):
    for name, score in results.items():
        if score == target_score:
            return name
    return None


def pair_comparison(results):
    students = list(results.items())
    pairs = []

    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            student1, score1 = students[i]
            student2, score2 = students[j]

            if score1 == score2:
                pairs.append((student1, student2, score1))

    return pairs


def display_results():
    print("\nQuiz Results")
    print("-" * 30)

    for name, score in quiz_results.items():
        print(f"{name}: {score}")


def main():
    while True:
        print("\nMy Quiz Result Searcher")
        print("1. Display quiz results")
        print("2. Direct access")
        print("3. Linear search")
        print("4. Pair comparison")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_results()

        elif choice == "2":
            name = input("Enter student name: ")
            result = direct_access(quiz_results, name)

            if result is not None:
                print(f"{name}'s score: {result}")
            else:
                print("Student not found.")

        elif choice == "3":
            try:
                target = int(input("Enter score to search for: "))
                result = linear_search(quiz_results, target)

                if result is not None:
                    print(f"{result} has a score of {target}.")
                else:
                    print("Score not found.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            pairs = pair_comparison(quiz_results)

            if pairs:
                print("\nStudents with matching scores:")
                for student1, student2, score in pairs:
                    print(f"{student1} and {student2}: {score}")
            else:
                print("No students have matching scores.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
