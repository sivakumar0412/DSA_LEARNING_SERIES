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


# Reverse an array (no built-in)
arr = [1, 2, 3, 4]
rev = []

for i in range(len(arr)-1, -1, -1):
    rev.append(arr[i])

print(rev)


## INTERMEDIATE DSA – SOLUTIONS
## Second largest element

arr = [10, 5, 20, 8]
largest = second = -1

for x in arr:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x

print(second)

# Missing number
arr = [1, 2, 4, 5]
n = 5
total = n * (n + 1) // 2
sum_arr = 0

for x in arr:
    sum_arr += x

print(total - sum_arr)

#Linear Search
arr = [4, 2, 7, 1]
target = 7

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index", i)
        break

# ADVANCED DSA – SOLUTIONS

# Two Sum (brute force)
arr = [2, 7, 11, 15]
target = 9

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(i, j)
