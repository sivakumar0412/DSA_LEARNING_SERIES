n = 5
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

# Method 2
# 5x5 star pattern
for i in range(5):
    print("*" * 5)

# Count digits in a number
num = 12345
count = 0

for i in str(num):
    count += 1

print(count)
