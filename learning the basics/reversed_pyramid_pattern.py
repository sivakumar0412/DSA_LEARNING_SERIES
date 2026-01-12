rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")

# Using While Loop
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1
