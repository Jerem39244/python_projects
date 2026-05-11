class Expression:
    def __init__(self, num1, num2, num3):
        # Constructor to initialize instance attributes
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calculate_addition(self):
        # Method to calculate and print the sum
        result = self.num1 + self.num2 + self.num3
        print(f"The sum of the three numbers is: {result}")

# Creating objects for implementation
obj1 = Expression(10, 20, 30)
obj1.calculate_addition()

obj2 = Expression(5.5, 4.5, 10)
obj2.calculate_addition()
