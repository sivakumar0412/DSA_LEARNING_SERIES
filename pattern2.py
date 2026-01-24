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

# Sum of subarray ranges


class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)

        def sumSubarrayMins():
            stack = []
            left = [0] * n
            right = [0] * n

            for i in range(n):
                count = 1
                while stack and stack[-1][0] > arr[i]:
                    count += stack.pop()[1]
                stack.append((arr[i], count))
                left[i] = count

            stack.clear()
            for i in range(n - 1, -1, -1):
                count = 1
                while stack and stack[-1][0] >= arr[i]:
                    count += stack.pop()[1]
                stack.append((arr[i], count))
                right[i] = count

            total = 0
            for i in range(n):
                total += arr[i] * left[i] * right[i]
            return total

        def sumSubarrayMaxs():
            stack = []
            left = [0] * n
            right = [0] * n

            for i in range(n):
                count = 1
                while stack and stack[-1][0] < arr[i]:
                    count += stack.pop()[1]
                stack.append((arr[i], count))
                left[i] = count

            stack.clear()

            for i in range(n - 1, -1, -1):
                count = 1
                while stack and stack[-1][0] <= arr[i]:
                    count += stack.pop()[1]
                stack.append((arr[i], count))
                right[i] = count

            total = 0
            for i in range(n):
                total += arr[i] * left[i] * right[i]
            return total

        # Final result
        return sumSubarrayMaxs() - sumSubarrayMins()

# Josephus problem


class Solution:
    def josephus(self, n, k):
        survivor = 0

        for i in range(1, n + 1):
            survivor = (survivor + k) % i

        return survivor + 1
