def python(i):
    if i < 2:
        return 1
    else:
        return i * python(i-1)


number = int(input("Enter a number:"))

result= python(number)
print(f"The Factorial of {number} is:{result}")
