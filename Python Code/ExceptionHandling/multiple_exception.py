def divison(a, b):
    try:
        if a > b:
            print(a // b)
        elif b > a:
            print(b // a)
        else:
            print(a, b)
    except TypeError:
        print("Please enter numbers only")
    except ZeroDivisionError:
        print("Zero division error")

# divison(0, 0)
try:
    number = int(input("Enter a number: "))
    print(100 / number)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")