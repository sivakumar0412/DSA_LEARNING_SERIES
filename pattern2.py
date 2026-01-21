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

# Stock span problem


class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        span = [0] * n
        stack = []   # stores indices

        for i in range(n):
            # Remove smaller or equal prices
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            # If stack empty, span is full length
            if not stack:
                span[i] = i + 1
            else:
                span[i] = i - stack[-1]

            # Push current index
            stack.append(i)

        return span
