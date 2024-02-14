print("yehtoh!")


# Create a function for fibonacci sequence
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()


# Create the algorithm for the fibonacci sequence
def fibonacci3(n):
    a = 0
    b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# print yehtoh 1000 times
for i in range(1000):
    print("yehtoh")