try:
    a = int(input("Enter The First Number:-"))
    b = int(input("Enter the secoend number:-"))
    print("What kind of operation do you want to perform.\nPress + " \
    "for addition\npress - for subtraction\npress / for division\npress * for multiplication")

    o = input("Enter Operation: ")
    match o:
        case "+":
            print(f"The result is:{a + b}")
        case "-":
            print(f"The result is:{a - b}")
        case "*":
            print(f"The result is:{a * b}")
        case "/":
            print(f"The result is:{a / b}")
        case default:
            print(f"There was an error")
except Exception as e:
    print("Enter a valid value of a and b")