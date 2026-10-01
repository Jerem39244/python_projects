#Enter your Binary: 010
#Decimal :  2
 #Enter your Binary: 1101
#Decimal :  13
# Binary to Decimal Converter


binary = input("Enter a binary number: ")


decimal = 0


for digit in binary:
    if digit != "0" and digit != "1":
        print("Invalid binary number!")
        break

    decimal = decimal * 2 + int(digit)

else:
    
    print("Decimal:", decimal)
