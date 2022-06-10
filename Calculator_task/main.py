# Python calculator that can perform: addition, subtraction, division, multiplication and modulus operations on two numbers
print("For Addition, enter 1")
print("For Subtraction, enter 2")
print("For Division, enter 3")
print("For Multiplication, enter 4")
print("For Modulus, enter 5\n")


while True:
    
    selection = input("Enter selection: ")
    if selection != "1" and selection != "2" and selection != "3" and selection != "4" and selection != "5":
        print("Please enter either:\n1 for Addition\n2 for Subtraction\n3 for Division\n4 for Multiplication, or\n5 for Modulus")

    else:
        print("Enter two numbers to calculate: ")
        x = input()
        y = input()

        try:
            num_1 = float(x)
            num_2 = float(y)

            if selection == "1":
                print(num_1 + num_2)

            elif selection == "2":
                print(num_1 - num_2)

            elif selection == "3":
                try:
                    print(num_1 / num_2)

                except:
                    print("Zero division error: division by zero")

            elif selection == "4":
                print(num_1 * num_2)

            elif selection == "5":
                try:
                    print(num_1 % num_2)

                except:
                    print("ZeroDivisionError: integer division or modulo by zero")

        except:
            print("Input is not a number. Please enter number.")

        
        print("Would you like to make another calculation?")
        quest = input("Enter Y/n: ")
        if quest == "Y" or quest == "y":
            pass
        else:
            break
