n = 4
# Upper
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()
# Lower
for i in range(n-1, 0, -1):
    for j in range(1, n-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()


# Using FUNCTION
def diamond(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "*"*(2*i-1))
    for i in range(n-1, 0, -1):
        print(" "*(n-i) + "*"*(2*i-1))


diamond(4)


# Using WHILE loop
n = 4
i = 1

while i <= n:
    print(" "*(n-i) + "*"*(2*i-1))
    i += 1

i = n-1
while i >= 1:
    print(" "*(n-i) + "*"*(2*i-1))
    i -= 1
