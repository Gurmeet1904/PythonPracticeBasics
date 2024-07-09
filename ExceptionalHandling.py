a = 5
b = 5

try:
    print("Resource Open")
    print(a/b)

    k = int(input("Enter a number: "))
    print(k)

except ZeroDivisionError as e:
    print("You cannot divide a number by zero. \nException message is: ", e)    # Here 'e' prints the division by zero exception message

except ValueError as e:
    print("Invalid input. \nException message is: " , e)

except Exception:
    print("Something went wrong")

finally:
    print("Resource closed")