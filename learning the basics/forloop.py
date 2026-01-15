# Sum of array elements
arr = [1, 2, 3, 4]
total = 0

for x in arr:
    total += x

print(total)

# Maximum and Minimum in array
arr = [7, 2, 9, 1]
maxi = arr[0]
mini = arr[0]

for x in arr:
    if x > maxi:
        maxi = x
    if x < mini:
        mini = x

print("Max:", maxi, "Min:", mini)
