n = 5
for i in range(n):
    print("*", end="")
    for j in range(i):
        print("*", end="")
    print()

# square pattern 
def square(rows):
    for i in range(rows):
        print("* " * rows)

square(5)