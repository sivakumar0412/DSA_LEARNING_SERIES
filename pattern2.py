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

# Max Circular Subarray Sum


class Solution:
    def maxCircularSum(self, arr):
        # Kadane for maximum subarray sum
        max_ending = max_so_far = arr[0]
        # Kadane for minimum subarray sum
        min_ending = min_so_far = arr[0]

        total_sum = arr[0]

        for i in range(1, len(arr)):
            x = arr[i]
            max_ending = max(x, max_ending + x)
            max_so_far = max(max_so_far, max_ending)

            min_ending = min(x, min_ending + x)
            min_so_far = min(min_so_far, min_ending)

            total_sum += x

        # If all elements are negative
        if max_so_far < 0:
            return max_so_far

        # Maximum of non-wrapping and wrapping cases
        return max(max_so_far, total_sum - min_so_far)

# Last Moment Before All Ants Fall Out


class Solution:
    def getLastMoment(self, n, left, right):
        last_time = 0

        # Ants moving left
        for pos in left:
            last_time = max(last_time, pos)

        # Ants moving right
        for pos in right:
            last_time = max(last_time, n - pos)

        return last_time

# Maximize Number of 1's


class Solution:
    def maxOnes(self, arr, k):
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(arr)):
            if arr[right] == 0:
                zero_count += 1

            # Shrink window if zeros exceed k
            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
# Max sum in the configuration


class Solution:
    def maxSum(self, arr):
        n = len(arr)

        # Step 1: Calculate sum of array
        arrSum = sum(arr)

        # Step 2: Calculate initial value of i*arr[i]
        currVal = 0
        for i in range(n):
            currVal += i * arr[i]

        maxVal = currVal

        # Step 3: Compute values for other rotations
        for i in range(1, n):
            currVal = currVal + arrSum - n * arr[n - i]
            maxVal = max(maxVal, currVal)

        return maxVal

# Find Kth Rotation


class Solution:
    def findKRotation(self, arr):
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high) // 2

            # Minimum lies in right part
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid

        # low is the index of minimum element
        return low

# Koko Eating Bananas


class Solution:
    def kokoEat(self, arr, k):
        import math

        left = 1
        right = max(arr)
        answer = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0

            # Calculate total hours needed at speed = mid
            for bananas in arr:
                hours += (bananas + mid - 1) // mid   # ceil division

            if hours <= k:
                answer = mid
                right = mid - 1   # try smaller speed
            else:
                left = mid + 1    # need faster speed

        return answer

# Equalize the Towers


class Solution:
    def minCost(self, heights, cost):
        def getCost(target):
            total = 0
            for h, c in zip(heights, cost):
                total += abs(h - target) * c
            return total

        low = min(heights)
        high = max(heights)

        answer = getCost(low)

        while low < high:
            mid = (low + high) // 2
            cost_mid = getCost(mid)
            cost_next = getCost(mid + 1)

            answer = min(answer, cost_mid, cost_next)

            if cost_mid > cost_next:
                low = mid + 1
            else:
                high = mid

        return answer
# Max min Height


class Solution:
    def maxMinHeight(self, arr, k, w):
        n = len(arr)

        def canReach(target):
            diff = [0] * (n + 1)
            water_used = 0
            curr_add = 0

            for i in range(n):
                curr_add += diff[i]
                current_height = arr[i] + curr_add

                if current_height < target:
                    need = target - current_height
                    water_used += need
                    if water_used > k:
                        return False

                    curr_add += need
                    if i + w < len(diff):
                        diff[i + w] -= need

            return True

        low = min(arr)
        high = min(arr) + k   # max possible min height

        answer = low
        while low <= high:
            mid = (low + high) // 2
            if canReach(mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1

        return answer
 
 # All numbers with specific difference


class Solution:
    def getCount(self, n, d):

        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        # If n is too small, brute check only
        limit = min(n, d + 162)

        count = 0
        for x in range(d, limit + 1):
            if x - digit_sum(x) >= d:
                count += 1

        # All numbers >= d+163 are guaranteed valid
        if n > d + 162:
            count += n - (d + 162)

        return count

# The Painter's Partition Problem-II


class Solution:
    def minTime(self, arr, k):
        # If painters >= boards, answer is max board
        if k >= len(arr):
            return max(arr)

        def canPaint(max_time):
            painters = 1
            curr_sum = 0

            for board in arr:
                if curr_sum + board <= max_time:
                    curr_sum += board
                else:
                    painters += 1
                    curr_sum = board
                    if painters > k:
                        return False
            return True

        low = max(arr)
        high = sum(arr)
        answer = high

        while low <= high:
            mid = (low + high) // 2

            if canPaint(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer
