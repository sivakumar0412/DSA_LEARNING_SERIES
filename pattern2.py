from collections import deque
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

# Number of Valid Parentheses


class Solution:
    def findWays(self, n):
        if n % 2 != 0:
            return 0

        pairs = n // 2
        dp = [0] * (pairs + 1)
        dp[0] = 1

        for i in range(1, pairs + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]

        return dp[pairs]


# Generate Permutations of an array
class Solution:
    def permuteDist(self, arr):
        res = []
        n = len(arr)
        used = [False] * n

        def backtrack(path):
            # If permutation is complete
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(arr[i])
                    backtrack(path)
                    path.pop()       # backtrack
                    used[i] = False

        backtrack([])
        return res

# Count Subset With Target Sum II


class Solution:
    def countSubset(self, arr, k):
        import bisect

        n = len(arr)
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        def gen_sums(nums, idx, curr, res):
            if idx == len(nums):
                res.append(curr)
                return
            gen_sums(nums, idx + 1, curr, res)
            gen_sums(nums, idx + 1, curr + nums[idx], res)

        leftSums = []
        rightSums = []

        gen_sums(left, 0, 0, leftSums)
        gen_sums(right, 0, 0, rightSums)
        rightSums.sort()

        count = 0
        for s in leftSums:
            target = k - s
            l = bisect.bisect_left(rightSums, target)
            r = bisect.bisect_right(rightSums, target)
            count += (r - l)

        return count


# Stream First Non-repeating


class Solution:
    def firstNonRepeating(self, s):
        freq = [0] * 26
        q = deque()
        result = []

        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] += 1
            q.append(ch)

            # Remove repeating characters from front
            while q and freq[ord(q[0]) - ord('a')] > 1:
                q.popleft()

            # Append answer for current prefix
            if q:
                result.append(q[0])
            else:
                result.append('#')

        return "".join(result)


# Interleave the First Half of the Queue with Second Half


class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        half = n // 2

        temp = deque()

        # Step 1: Move first half to temp queue
        for _ in range(half):
            temp.append(q.popleft())

        # Step 2: Interleave both halves
        while temp:
            q.append(temp.popleft())
            q.append(q.popleft())

        return q


# Implement k Queues in a Single Array
class kQueues:
    def __init__(self, n, k):
        self.n = n
        self.k = k

        self.arr = [0] * n
        self.front = [-1] * k
        self.rear = [-1] * k
        self.next = list(range(1, n)) + [-1]

        self.free = 0

    def enqueue(self, x, i):
        if self.free == -1:
            return
        index = self.free
        self.free = self.next[index]

        if self.front[i] == -1:
            self.front[i] = index
        else:
            self.next[self.rear[i]] = index

        self.next[index] = -1
        self.rear[i] = index
        self.arr[index] = x

    def dequeue(self, i):
        if self.front[i] == -1:
            return -1

        index = self.front[i]
        self.front[i] = self.next[index]

        # Add this index back to free list
        self.next[index] = self.free
        self.free = index

        return self.arr[index]

    def isEmpty(self, i):
        return self.front[i] == -1

    def isFull(self):
        return self.free == -1


# K Sized Subarray Maximum
class Solution:
    def maxOfSubarrays(self, arr, k):
        dq = deque()
        result = []

        for i in range(len(arr)):

            # Remove indexes that are out of this window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from back
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()

            dq.append(i)

            # When first window is completed
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result
