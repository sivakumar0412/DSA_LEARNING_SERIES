from collections import defaultdict
from functools import cmp_to_key
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
# Meeting Rooms


class Solution:
    def canAttend(self, arr):
        # Sort meetings by start time
        arr.sort(key=lambda x: x[0])

        # Check for overlap
        for i in range(1, len(arr)):
            # If current meeting starts before previous ends
            if arr[i][0] < arr[i - 1][1]:
                return False

        return True

#Maximum number of overlapping Intervals


class Solution:
    def overlapInt(self, arr):
        n = len(arr)

        start = []
        end = []

        for s, e in arr:
            start.append(s)
            end.append(e)

        start.sort()
        end.sort()

        i = 0
        j = 0
        curr = 0
        max_overlap = 0

        while i < n and j < n:
            # Since intervals are inclusive,
            # start <= end means overlap
            if start[i] <= end[j]:
                curr += 1
                max_overlap = max(max_overlap, curr)
                i += 1
            else:
                curr -= 1
                j += 1

        return max_overlap

# Count Inversions


class Solution:
    def inversionCount(self, arr):

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, inv_left = merge_sort(arr[:mid])
            right, inv_right = merge_sort(arr[mid:])

            merged = []
            i = j = 0
            inv_count = inv_left + inv_right

            # Merge step
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    inv_count += len(left) - i
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged, inv_count

        _, count = merge_sort(arr)
        return count

# Missing Element in Range


class Solution:
    def missingRange(self, arr, low, high):
        s = set(arr)
        result = []

        for num in range(low, high + 1):
            if num not in s:
                result.append(num)

        return result

# Form the Largest Number


class Solution:
    def findLargest(self, arr):
        # Convert to string
        arr = list(map(str, arr))

        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        # Sort using comparator
        arr.sort(key=cmp_to_key(compare))

        # Join result
        result = ''.join(arr)

        # Edge case: all zeros
        return '0' if result[0] == '0' else result

# Find H-Index


class Solution:
    def hIndex(self, citations):
        # Sort in descending order
        citations.sort(reverse=True)

        h = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break

        return h

# Count Subarrays with given XOR


class Solution:
    def subarrayXor(self, arr, k):
        freq = {0: 1}   # prefix XOR 0 occurs once
        xr = 0
        count = 0

        for num in arr:
            xr ^= num

            # If (xr ^ k) seen before, add its count
            count += freq.get(xr ^ k, 0)

            # Update frequency of current prefix XOR
            freq[xr] = freq.get(xr, 0) + 1

        return count

# Union of Arrays with Duplicates
class Solution:
    def findUnion(self, a, b):
        # Use set to remove duplicates
        result = set(a) | set(b)
        return list(result)

# Longest Span in two Binary Arrays


class Solution:
    def equalSumSpan(self, a1, a2):
        prefix_sum = 0
        first_occ = {0: -1}   # sum 0 seen before index 0
        max_len = 0

        for i in range(len(a1)):
            prefix_sum += a1[i] - a2[i]

            if prefix_sum in first_occ:
                max_len = max(max_len, i - first_occ[prefix_sum])
            else:
                first_occ[prefix_sum] = i

        return max_len

# Longest Subarray with Majority Greater than K


class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)

        # Step 1: Convert to +1 / -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + (1 if arr[i] > k else -1)

        # Step 2: Build decreasing stack
        stack = []
        for i in range(n + 1):
            if not stack or prefix[i] < prefix[stack[-1]]:
                stack.append(i)

        # Step 3: Traverse from right to left
        ans = 0
        for j in range(n, -1, -1):
            while stack and prefix[j] > prefix[stack[-1]]:
                ans = max(ans, j - stack[-1])
                stack.pop()

        return ans

# Isomorphic Strings
class Solution:
    def areIsomorphic(self, s1, s2):
        map1 = {}
        map2 = {}

        for c1, c2 in zip(s1, s2):
            # Check s1 -> s2 mapping
            if c1 in map1:
                if map1[c1] != c2:
                    return False
            else:
                map1[c1] = c2

            # Check s2 -> s1 mapping
            if c2 in map2:
                if map2[c2] != c1:
                    return False
            else:
                map2[c2] = c1

        return True

# Find the closest pair from two arrays


class Solution:
    def findClosestPair(self, arr1, arr2, x):
        n = len(arr1)
        m = len(arr2)

        i = 0
        j = m - 1

        min_diff = float('inf')
        result = [0, 0]

        while i < n and j >= 0:
            curr_sum = arr1[i] + arr2[j]
            diff = abs(curr_sum - x)

            if diff < min_diff:
                min_diff = diff
                result = [arr1[i], arr2[j]]

            if curr_sum > x:
                j -= 1
            else:
                i += 1

        return result

# Move All Zeroes to End
class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        pos = 0  # position to place next non-zero element

        # Move all non-zero elements to the front
        for i in range(n):
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos += 1

        # Fill remaining positions with zeros
        while pos < n:
            arr[pos] = 0
            pos += 1

# Trapping Rain Water


class Solution:
    def maxWater(self, arr):
        n = len(arr)
        left = 0
        right = n - 1

        left_max = 0
        right_max = 0
        water = 0

        while left <= right:
            if arr[left] <= arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water += right_max - arr[right]
                right -= 1

        return water

# Longest subarray with Atmost two distinct integers
class Solution:
    def totalElements(self, arr):
        left = 0
        freq = {}
        max_len = 0

        for right in range(len(arr)):
            # Add current element
            freq[arr[right]] = freq.get(arr[right], 0) + 1

            # If more than 2 distinct, shrink window
            while len(freq) > 2:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1

            # Update maximum length
            max_len = max(max_len, right - left + 1)

        return max_len

# Max Xor Subarray of size K


class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)

        # XOR of first window
        curr_xor = 0
        for i in range(k):
            curr_xor ^= arr[i]

        max_xor = curr_xor

        # Slide window
        for i in range(k, n):
            curr_xor ^= arr[i - k]  # remove left
            curr_xor ^= arr[i]      # add new element
            max_xor = max(max_xor, curr_xor)

        return max_xor

# Longest Substring with K Uniques


class Solution:
    def longestKSubstr(self, s, k):
        left = 0
        freq = {}
        max_len = -1

        for right in range(len(s)):
            # Add character to window
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Shrink window if distinct > k
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            # Update max length when exactly k distinct
            if len(freq) == k:
                max_len = max(max_len, right - left + 1)

        return max_len

# Smallest window containing all characters
class Solution:
    def minWindow(self, s, p):
        from collections import Counter
        
        freq = Counter(p)
        need = len(p)
        left = 0
        min_len = float('inf')
        start = 0
        
        for right in range(len(s)):
            if freq[s[right]] > 0:
                need -= 1
            freq[s[right]] -= 1
            
            # When all characters matched
            while need == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                
                freq[s[left]] += 1
                if freq[s[left]] > 0:
                    need += 1
                left += 1
        
        if min_len == float('inf'):
            return ""
        
        return s[start:start + min_len]

# Dice throw


class Solution:
    def noOfWays(self, m, n, x):
        # DP table
        dp = [[0] * (x + 1) for _ in range(n + 1)]

        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, x + 1):
                for f in range(1, m + 1):
                    if j - f >= 0:
                        dp[i][j] += dp[i-1][j-f]

        return dp[n][x]

# Pythagorean Triplet
class Solution:
    def pythagoreanTriplet(self, arr):
        n = len(arr)

        # square all values
        squares = set(x*x for x in arr)

        arr = [x*x for x in arr]

        for i in range(n):
            for j in range(i+1, n):
                if arr[i] + arr[j] in squares:
                    return True

        return False

# Largest number in one swap

class Solution:
    def largestSwap(self, s):
        arr = list(s)
        n = len(arr)

        # store last index of each digit
        last = [-1]*10
        for i in range(n):
            last[int(arr[i])] = i

        # try to improve from left to right
        for i in range(n):
            current = int(arr[i])

            for d in range(9, current, -1):
                if last[d] > i:
                    arr[i], arr[last[d]] = arr[last[d]], arr[i]
                    return "".join(arr)

        return s

# Subarrays with First Element Minimum

class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        ans = 0
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                ans += i - idx
            stack.append(i)
        
        while stack:
            idx = stack.pop()
            ans += n - idx
        
        return ans

# Sum of subarray minimums


class Solution:
    def sumSubMins(self, arr):
        n = len(arr)

        prev = [-1]*n
        next_ = [n]*n

        stack = []

        # Previous Less Element
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        # Next Less Element
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0

        for i in range(n):
            left = i - prev[i]
            right = next_[i] - i
            ans += arr[i] * left * right

        return ans

# Minimum K Consecutive Bit Flips


class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        is_flipped = [0] * n
        flip = 0
        ans = 0

        for i in range(n):
            # remove effect of flip window that ended
            if i >= k:
                flip ^= is_flipped[i - k]

            # current bit after flips
            current = arr[i] ^ flip

            # if current bit is 0, we must flip here
            if current == 0:
                if i + k > n:
                    return -1
                is_flipped[i] = 1
                flip ^= 1
                ans += 1

        return ans


# Generate IP Addresses
class Solution:
    def generateIp(self, s):
        res = []
        n = len(s)

        def valid(part):
            if len(part) > 1 and part[0] == '0':
                return False
            return 0 <= int(part) <= 255

        def backtrack(start, parts, path):
            if parts == 4 and start == n:
                res.append(".".join(path))
                return

            if parts == 4:
                return

            for length in range(1, 4):
                if start + length <= n:
                    part = s[start:start+length]
                    if valid(part):
                        backtrack(start+length, parts+1, path+[part])

        backtrack(0, 0, [])
        return res

# Top View of Binary Tree


class Solution:
    def topView(self, root):
        if not root:
            return []

        q = deque()
        q.append((root, 0))   # (node, horizontal distance)

        top = {}

        while q:
            node, hd = q.popleft()

            # store first node at this horizontal distance
            if hd not in top:
                top[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))

            if node.right:
                q.append((node.right, hd + 1))

        # sort by horizontal distance
        result = []
        for key in sorted(top.keys()):
            result.append(top[key])

        return result


# K Sum Paths


class Solution:
    def countAllPaths(self, root, k):
        prefix = defaultdict(int)
        prefix[0] = 1
        count = 0

        def dfs(node, curr_sum):
            nonlocal count
            if not node:
                return

            curr_sum += node.data

            # check if path with sum k ends here
            count += prefix[curr_sum - k]

            prefix[curr_sum] += 1

            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            # backtrack
            prefix[curr_sum] -= 1

        dfs(root, 0)
        return count


# Burning Tree


class Solution:
    def minTime(self, root, target):

        # Step 1: Build parent mapping
        parent = {}
        target_node = None

        def dfs(node, par):
            nonlocal target_node
            if not node:
                return

            parent[node] = par

            if node.data == target:
                target_node = node

            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        # Step 2: BFS (burning process)
        q = deque([target_node])
        visited = set([target_node])

        time = 0

        while q:
            size = len(q)
            burned = False

            for _ in range(size):
                node = q.popleft()

                for neighbor in [node.left, node.right, parent[node]]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                        burned = True

            if burned:
                time += 1

        return time

# Distribute Candies

class Solution:
    def distCandy(self, root):
        self.moves = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # count moves
            self.moves += abs(left) + abs(right)

            # return net candies to parent
            return node.data + left + right - 1

        dfs(root)
        return self.moves

# Largest BST


class Solution:
    def largestBst(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return (True, 0, float('inf'), float('-inf'))
                # (isBST, size, min, max)

            left = dfs(node.left)
            right = dfs(node.right)

            # check BST condition
            if left[0] and right[0] and left[3] < node.data < right[2]:
                size = left[1] + right[1] + 1
                self.ans = max(self.ans, size)

                return (
                    True,
                    size,
                    min(node.data, left[2]),
                    max(node.data, right[3])
                )
            else:
                return (False, 0, 0, 0)

        dfs(root)
        return self.ans

# Predecessor and Successor


class Solution:
    def findPreSuc(self, root, key):
        pre = None
        suc = None

        curr = root

        while curr:
            if curr.data < key:
                pre = curr
                curr = curr.right
            elif curr.data > key:
                suc = curr
                curr = curr.left
            else:
                # predecessor (max in left subtree)
                if curr.left:
                    temp = curr.left
                    while temp.right:
                        temp = temp.right
                    pre = temp

                # successor (min in right subtree)
                if curr.right:
                    temp = curr.right
                    while temp.left:
                        temp = temp.left
                    suc = temp

                break

        return pre, suc


# Number of BST From Array
class Solution:
    def countBSTs(self, arr):
        n = len(arr)

        # Precompute Catalan numbers up to n
        catalan = [0] * (n + 1)
        catalan[0] = catalan[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]

        result = []

        for val in arr:
            left = 0
            right = 0

            for x in arr:
                if x < val:
                    left += 1
                elif x > val:
                    right += 1

            result.append(catalan[left] * catalan[right])

        return result


# Rotten Oranges


class Solution:
    def orangesRot(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        q = deque()
        fresh = 0

        # Step 1: Collect rotten oranges & count fresh
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 2:
                    q.append((i, j))
                elif mat[i][j] == 1:
                    fresh += 1

        # If no fresh oranges
        if fresh == 0:
            return 0

        time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 2: BFS
        while q:
            size = len(q)
            rotted = False

            for _ in range(size):
                x, y = q.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and mat[nx][ny] == 1:
                        mat[nx][ny] = 2
                        q.append((nx, ny))
                        fresh -= 1
                        rotted = True

            if rotted:
                time += 1

        return time if fresh == 0 else -1


# Length of Longest Cycle in a Graph
class Solution:
    def longestCycle(self, V, edges):
        # create adjacency (each node has at most one outgoing)
        graph = [-1] * V
        for u, v in edges:
            graph[u] = v

        visited = [False] * V
        ans = -1

        for i in range(V):
            if visited[i]:
                continue

            curr = i
            step_map = {}   # node → step
            step = 0

            while curr != -1 and not visited[curr]:
                visited[curr] = True
                step_map[curr] = step
                step += 1
                curr = graph[curr]

                # cycle detected
                if curr in step_map:
                    cycle_len = step - step_map[curr]
                    ans = max(ans, cycle_len)
                    break

        return ans

# Course Schedule I
from collections import deque

class Solution:
    def canFinish(self, n, prerequisites):
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        # Build graph
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1

        # Queue for nodes with 0 indegree
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        count = 0

        # Topological sort
        while q:
            node = q.popleft()
            count += 1

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return count == n


# Minimum height roots


class Solution:
    def minHeightRoot(self, V, edges):
        if V == 1:
            return [0]

        graph = [[] for _ in range(V)]
        degree = [0] * V

        # Build graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Initial leaves
        q = deque()
        for i in range(V):
            if degree[i] == 1:
                q.append(i)

        remaining = V

        # Remove leaves layer by layer
        while remaining > 2:
            size = len(q)
            remaining -= size

            for _ in range(size):
                node = q.popleft()

                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)

        return list(q)

# Number of Ways to Arrive at Destination
import heapq

class Solution:
    def countPaths(self, V, edges):
        MOD = 10**9 + 7

        # Build graph
        graph = [[] for _ in range(V)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Dijkstra setup
        dist = [float('inf')] * V
        ways = [0] * V

        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]  # (distance, node)

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for nei, w in graph[node]:
                new_dist = d + w

                # shorter path found
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (new_dist, nei))

                # another shortest path
                elif new_dist == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD

        return ways[V - 1] % MOD

# Articulation Point - II


class Solution:
    def articulationPoints(self, V, edges):
        # build graph
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * V
        low = [-1] * V
        parent = [-1] * V
        visited = [False] * V
        ap = [False] * V

        time = 0

        def dfs(u):
            nonlocal time
            visited[u] = True
            disc[u] = low[u] = time
            time += 1
            children = 0

            for v in graph[u]:
                if not visited[v]:
                    parent[v] = u
                    children += 1
                    dfs(v)

                    low[u] = min(low[u], low[v])

                    # Case 1: root
                    if parent[u] == -1 and children > 1:
                        ap[u] = True

                    # Case 2: non-root
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True

                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])

        # handle disconnected graph
        for i in range(V):
            if not visited[i]:
                dfs(i)

        result = [i for i in range(V) if ap[i]]

        return result if result else [-1]

# Partitions with Given Difference


class Solution:
    def countPartitions(self, arr, diff):
        total = sum(arr)

        # not possible
        if (total + diff) % 2 != 0:
            return 0

        target = (total + diff) // 2

        # DP array
        dp = [0] * (target + 1)
        dp[0] = 1   # one way to make sum 0

        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[target]

# Minimum cost to connect all houses in a city


class Solution:
    def minCost(self, houses):
        n = len(houses)
        visited = [False] * n

        minHeap = [(0, 0)]  # (cost, node)
        total_cost = 0
        edges_used = 0

        while edges_used < n:
            cost, u = heapq.heappop(minHeap)

            if visited[u]:
                continue

            visited[u] = True
            total_cost += cost
            edges_used += 1

            # explore all neighbors
            for v in range(n):
                if not visited[v]:
                    dist = abs(houses[u][0] - houses[v][0]) + \
                        abs(houses[u][1] - houses[v][1])
                    heapq.heappush(minHeap, (dist, v))

        return total_cost

# Buy Stock with Transaction Fee


class Solution:
    def maxProfit(self, arr, k):
        if not arr:
            return 0

        hold = -arr[0]   # buying first stock
        cash = 0         # no stock

        for price in arr[1:]:
            # update hold and cash
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - k)

        return cash

# Painting the Fence
class Solution:
    def countWays(self, n, k):
        # Base case: if only one post, we can paint it in k ways
        if n == 1:
            return k
        
        # For two posts:
        same = k          # both posts same color
        diff = k * (k - 1)  # both posts different colors
        
        # For posts from 3 to n
        for i in range(3, n + 1):
            new_same = diff
            new_diff = (same + diff) * (k - 1)
            same, diff = new_same, new_diff
        
        return same + diff

# Print Diagonally
class Solution:
    def diagView(self, mat):
        n = len(mat)
        result = []

        # upper half (first row)
        for col in range(n):
            i = 0
            j = col
            while i < n and j >= 0:
                result.append(mat[i][j])
                i += 1
                j -= 1

        # lower half (last column)
        for row in range(1, n):
            i = row
            j = n - 1
            while i < n and j >= 0:
                result.append(mat[i][j])
                i += 1
                j -= 1

        return result

# Gray Code


class Solution:
    def graycode(self, n):
        res = [""]

        for i in range(n):
            temp = []

            # prefix 0
            for code in res:
                temp.append("0" + code)

            # prefix 1 (reverse)
            for code in reversed(res):
                temp.append("1" + code)

            res = temp

        return res

# Huffman Encoding
import heapq

class Node:
    def __init__(self, char, freq, idx):
        self.char = char
        self.freq = freq
        self.idx = idx   # tie-breaker: order of appearance
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.idx < other.idx
        return self.freq < other.freq

class Solution:
    def huffmanCodes(self, s, f):
        # Edge case: only one character
        if len(s) == 1:
            return ["0"]

        # Step 1: Build heap
        heap = []
        for i in range(len(s)):
            heapq.heappush(heap, Node(s[i], f[i], i))
        
        # Step 2: Build Huffman Tree
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = Node(None, left.freq + right.freq, min(left.idx, right.idx))
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)
        
        root = heap[0]
        
        # Step 3: Preorder traversal to collect codes
        codes = []
        def preorder(node, code):
            if node is None:
                return
            if node.char is not None:  # leaf node
                codes.append(code)
            preorder(node.left, code + "0")
            preorder(node.right, code + "1")
        
        preorder(root, "")
        return codes
# Segregate 0s and 1s


class Solution:
    def segregate0and1(self, arr):
        # Step 1: Count number of 0s
        count_zeros = arr.count(0)

        # Step 2: Fill first count_zeros positions with 0
        for i in range(count_zeros):
            arr[i] = 0

        # Step 3: Fill remaining positions with 1
        for i in range(count_zeros, len(arr)):
            arr[i] = 1

        return arr

# Intersection of Two Sorted Arrays
class Solution:
    def intersection(self, a, b):
        i, j = 0, 0
        result = []
        
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                # Add only distinct elements
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        
        return result
# Toeplitz matrix


class Solution:
    def isToeplitz(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        # Check diagonals
        for i in range(1, rows):
            for j in range(1, cols):
                if mat[i][j] != mat[i-1][j-1]:
                    return False
        return True

# Next Smallest Palindrome
class Solution:
    def nextPalindrome(self, num):
        n = len(num)
        
        # Step 1: Create a copy
        result = num[:]
        
        # Step 2: Mirror left to right
        for i in range(n // 2):
            result[n - i - 1] = result[i]
        
        # Step 3: Check if result > num
        if result > num:
            return result
        
        # Step 4: Add 1 to middle
        carry = 1
        mid = n // 2
        
        # If odd length
        if n % 2 == 1:
            result[mid] += carry
            carry = result[mid] // 10
            result[mid] %= 10
            left = mid - 1
            right = mid + 1
        else:
            left = mid - 1
            right = mid
        
        # Handle carry
        while left >= 0 and carry:
            result[left] += carry
            carry = result[left] // 10
            result[left] %= 10
            result[right] = result[left]
            left -= 1
            right += 1
        
        # If still carry (like 999 → 1001)
        if carry:
            result = [1] + [0] * (n - 1) + [1]
            return result
        
        # Final mirror
        while left >= 0:
            result[right] = result[left]
            left -= 1
            right += 1
        
        return result
        
# Implement Atoi


class Solution:
    def myAtoi(self, s):
        # Step 1: Trim leading whitespaces
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Handle sign
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        # Step 3: Read digits
        result = 0
        while index < len(s) and s[index].isdigit():
            digit = ord(s[index]) - ord('0')  # convert char to int
            result = result * 10 + digit
            index += 1

        # Step 4: Apply sign
        result *= sign

        # Step 5: Handle overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result

# Anagram Palindrome
class Solution:
    def canFormPalindrome(self, s):
        # Step 1: Count frequency of each character
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        # Step 2: Count odd occurrences
        odd_count = 0
        for count in freq.values():
            if count % 2 != 0:
                odd_count += 1
        
        # Step 3: Check palindrome condition
        return odd_count <= 1

# Flip to Maximize 1s
class Solution:
    def maxOnes(self, arr):
        # Step 1: Count original 1s
        original_ones = sum(arr)
        
        # Step 2: Transform array (0 -> +1, 1 -> -1)
        transformed = [1 if x == 0 else -1 for x in arr]
        
        # Step 3: Kadane's algorithm to find max subarray sum
        max_gain = float('-inf')
        current_sum = 0
        for val in transformed:
            current_sum = max(val, current_sum + val)
            max_gain = max(max_gain, current_sum)
        
        # Step 4: If all are 1s, no flip improves result
        if original_ones == len(arr):
            return original_ones
        
        # Step 5: Add best gain to original 1s
        return original_ones + max_gain

# Count Derangements


class Solution:
    def derangeCount(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 1
        if n == 1:
            return 0

        # DP array
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 0

        # Fill using recurrence
        for i in range(2, n + 1):
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])

        return dp[n]

# Mean of range in array


class Solution:
    def findMean(self, arr, queries):
        n = len(arr)

        # Step 1: Build prefix sum
        prefix = [0] * n
        prefix[0] = arr[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + arr[i]

        # Step 2: Answer queries
        result = []
        for l, r in queries:
            total = prefix[r] - (prefix[l-1] if l > 0 else 0)
            length = r - l + 1
            result.append(total // length)  # floor division
        return result

# Two Equal Sum Subarrays
class Solution:
    def canSplit(self, arr):
        total_sum = sum(arr)
        
        # If total sum is odd, cannot split equally
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        prefix_sum = 0
        
        # Check if any prefix equals target
        for num in arr:
            prefix_sum += num
            if prefix_sum == target:
                return True
        
        return False

# Common in 3 Sorted Arrays


class Solution:
    def commonElements(self, a, b, c):
        i, j, k = 0, 0, 0
        res = []

        while i < len(a) and j < len(b) and k < len(c):
            # Case 1: All three are equal
            if a[i] == b[j] == c[k]:
                # Avoid duplicates
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
                j += 1
                k += 1

            # Case 2: Move the smallest pointer
            elif a[i] < b[j]:
                i += 1
            elif b[j] < c[k]:
                j += 1
            else:
                k += 1

        return res

# Min Swaps to Group 1s
class Solution:
    def minSwaps(self, arr):
        total_ones = sum(arr)
        if total_ones == 0:
            return -1
        
        # Initial window of size total_ones
        window_ones = sum(arr[:total_ones])
        max_ones = window_ones
        
        # Sliding window
        for i in range(total_ones, len(arr)):
            window_ones += arr[i] - arr[i - total_ones]
            max_ones = max(max_ones, window_ones)
        
        # Minimum swaps = missing ones in best window
        return total_ones - max_ones

# Check if an Array is Max Heap
class Solution:
    def isMaxHeap(self, arr):
        n = len(arr)
        
        # Only check non-leaf nodes
        for i in range(n // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            
            # Check left child
            if left < n and arr[i] < arr[left]:
                return False
            
            # Check right child
            if right < n and arr[i] < arr[right]:
                return False
        
        return True

# Kth Largest in a Stream
import heapq

class Solution:
    def kthLargest(self, arr, k):
        heap = []
        result = []
        
        for num in arr:
            heapq.heappush(heap, num)
            
            if len(heap) > k:
                heapq.heappop(heap)
            
            if len(heap) < k:
                result.append(-1)
            else:
                result.append(heap[0])
        
        return result

# Position of the Set Bit
import math

class Solution:
    def findPosition(self, n):
        # Case 1: n must be > 0 and power of 2
        if n > 0 and (n & (n - 1)) == 0:
            # Position = log2(n) + 1
            return int(math.log2(n)) + 1
        else:
            return -1

# Palindrome Binary
class Solution:
    def isBinaryPalindrome(self, n):
        # Step 1: Convert to binary string
        binary_str = bin(n)[2:]  # remove '0b' prefix
        
        # Step 2: Check if palindrome
        return binary_str == binary_str[::-1]

# Remove Invalid Parentheses
class Solution:
    def validParenthesis(self, s):

        # function to check string is valid or not
        def isValid(st):
            balance = 0

            for ch in st:

                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                # if closing bracket comes extra
                if balance < 0:
                    return False

            # at end balance should be 0
            return balance == 0


        from collections import deque

        q = deque()
        visited = set()
        ans = []

        q.append(s)
        visited.add(s)

        found = False

        while q:

            curr = q.popleft()

            # check current string valid or not
            if isValid(curr):
                ans.append(curr)
                found = True

            # if valid string found,
            # don't remove more brackets
            if found:
                continue

            # remove one bracket at every position
            for i in range(len(curr)):

                # skip normal characters
                if curr[i] not in '()':
                    continue

                newStr = curr[:i] + curr[i+1:]

                if newStr not in visited:
                    visited.add(newStr)
                    q.append(newStr)

        return sorted(list(set(ans)))

# Palindrome Pairs
class Solution:
    def palindromePair(self, arr):
        # Step 1: Map each word to its index
        word_map = {word: i for i, word in enumerate(arr)}
        
        # Helper function to check palindrome
        def is_palindrome(s):
            return s == s[::-1]
        
        # Step 2: Iterate through each word
        for i, word in enumerate(arr):
            n = len(word)
            
            # Split word into prefix and suffix
            for cut in range(n + 1):
                prefix, suffix = word[:cut], word[cut:]
                
                # Case 1: If prefix is palindrome, check reversed suffix
                if is_palindrome(prefix):
                    rev_suffix = suffix[::-1]
                    if rev_suffix in word_map and word_map[rev_suffix] != i:
                        return True
                
                # Case 2: If suffix is palindrome, check reversed prefix
                # (cut != n avoids duplicate check when suffix is empty)
                if cut != n and is_palindrome(suffix):
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_map and word_map[rev_prefix] != i:
                        return True
        
        return False

# Mother Vertex
class Solution:
    def findMotherVertex(self, V, edges):
        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)

        # Helper DFS
        def dfs(node, visited):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, visited)

        # Step 1: Find candidate by last finished DFS
        visited = [False] * V
        candidate = -1
        for i in range(V):
            if not visited[i]:
                dfs(i, visited)
                candidate = i

        # Step 2: Verify candidate
        visited = [False] * V
        dfs(candidate, visited)

        if all(visited):
            return candidate
        return -1

# Special Keyboard
class Solution:
    def optimalKeys(self, n: int) -> int:
        # DP array to store max 'A's for each keystroke count
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Option 1: Just press 'A'
            dp[i] = dp[i - 1] + 1

            # Option 2: Use Ctrl+A, Ctrl+C, then multiple Ctrl+V
            for j in range(1, i - 2):  # j is the point where we copy
                dp[i] = max(dp[i], dp[j] * (i - j - 1))

        return dp[n]

# Make the array beautiful
class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        
        stack = []

        for num in arr:

            # if signs are different
            if stack and ((stack[-1] >= 0 and num < 0) or 
                          (stack[-1] < 0 and num >= 0)):
                stack.pop()

            else:
                stack.append(num)

        return stack


# Minimum Multiplications to reach End


class Solution:
    def minSteps(self, arr, start, end):
        # If start is already equal to end
        if start == end:
            return 0

        # Queue for BFS: (value, steps)
        q = deque([(start, 0)])

        # Visited states (0-999)
        visited = [False] * 1000
        visited[start] = True

        while q:
            val, steps = q.popleft()

            for num in arr:
                nxt = (val * num) % 1000
                if not visited[nxt]:
                    if nxt == end:
                        return steps + 1
                    visited[nxt] = True
                    q.append((nxt, steps + 1))

        return -1

# Product Pair
class Solution:
    def isProduct(self, arr, target):
        seen = set()
        
        for num in arr:
            # Special case: target = 0
            if target == 0:
                if num == 0 or 0 in seen:
                    return True
            
            # Avoid division by zero
            if num != 0 and target % num == 0:
                complement = target // num
                if complement in seen:
                    return True
            
            seen.add(num)
        
        return False

# 1s Surrounded by 0s


class Solution:
    def cntOnes(self, grid):
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(i, j):
            from collections import deque
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if grid[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

        # Step 1: Start BFS from boundary 1s
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and grid[i][j] == 1 and not visited[i][j]:
                    bfs(i, j)

        # Step 2: Count trapped 1s
        trapped = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    trapped += 1

        return trapped

# Transform to Sum Tree
# Structure for Tree Node


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def toSumTree(self, root):
        # Helper function to recursively transform
        def transform(node):
            if node is None:
                return 0

            # Recursively transform left and right subtrees
            left_sum = transform(node.left)
            right_sum = transform(node.right)

            # Store original value before updating
            old_val = node.data

            # Update current node's value
            node.data = left_sum + right_sum

            # Return sum including original value (for parent's calculation)
            return node.data + old_val

        transform(root)

# Elements in the Range
class Solution:
    def checkElements(self, start, end, arr):
        # Convert array to set for fast lookup
        arr_set = set(arr)
        
        # Check if every element in range [start, end] exists in arr_set
        for num in range(start, end + 1):
            if num not in arr_set:
                return False
        return True

# Minimum Toggle to Partition
class Solution:
    def minToggle(self, arr):
        n = len(arr)
        
        total_zeros = arr.count(0)
        ones_left = 0
        zeros_right = total_zeros
        min_toggles = float('inf')
        
        # Case 1: partition before first element (all 1s)
        min_toggles = min(min_toggles, zeros_right)
        
        for num in arr:
            # Update counts
            if num == 1:
                ones_left += 1
            else:
                zeros_right -= 1
            
            # Case 2: partition after this element
            min_toggles = min(min_toggles, ones_left + zeros_right)
        
        # Case 3: partition after last element (all 0s)
        min_toggles = min(min_toggles, ones_left)
        
        return min_toggles

# Wifi Range
class Solution:
    def wifiRange(self, s, x):
        n = len(s)
        diff = [0] * (n + 1)
        
        for i in range(n):
            if s[i] == '1':
                left = max(0, i - x)
                right = min(n, i + x + 1)
                diff[left] += 1
                diff[right] -= 1
        
        coverage = 0
        for i in range(n):
            coverage += diff[i]
            if coverage == 0:  # room not covered
                return False
        
        return True

# Vertical Sum
# Structure of binary tree node


class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class Solution:
    def verticalSum(self, root):
        if not root:
            return []

        # Dictionary to store sums by horizontal distance
        hd_map = {}

        # Helper function for DFS traversal
        def dfs(node, hd):
            if not node:
                return
            # Add node value to its horizontal distance sum
            hd_map[hd] = hd_map.get(hd, 0) + node.data
            # Recurse left and right
            dfs(node.left, hd - 1)
            dfs(node.right, hd + 1)

        # Start DFS from root with hd = 0
        dfs(root, 0)

        # Collect results sorted by horizontal distance
        result = [hd_map[hd] for hd in sorted(hd_map.keys())]
        return result

# Count Sorted Digit Groupings

class Solution:
    def validGroups(self, s: str) -> int:
        from functools import lru_cache

        # Helper to compute digit sum of substring
        def digit_sum(sub: str) -> int:
            return sum(int(ch) for ch in sub)

        @lru_cache(None)
        def dfs(index: int, prev_sum: int) -> int:
            # If we've consumed the whole string, that's one valid grouping
            if index == len(s):
                return 1

            total = 0
            # Try all possible splits starting at index
            curr_sum = 0
            for j in range(index, len(s)):
                curr_sum += int(s[j])  # incremental sum
                if curr_sum >= prev_sum:
                    total += dfs(j + 1, curr_sum)
            return total

        return dfs(0, 0)

# Replace with XOR of Adjacent
class Solution:
    def replaceElements(self, arr):
        n = len(arr)
        if n < 2:
            return arr  # edge case, though constraints say n >= 2

        # Copy original array to avoid overwriting
        old = arr[:]

        # First element
        arr[0] = old[0] ^ old[1]

        # Middle elements
        for i in range(1, n - 1):
            arr[i] = old[i - 1] ^ old[i + 1]

        # Last element
        arr[n - 1] = old[n - 2] ^ old[n - 1]

        return arr

# Pairs with certain difference
class Solution:
    def sumDiffPairs(self, arr, k):
        arr.sort()
        ans = 0
        i = len(arr) - 1

        while i > 0:
            if arr[i] - arr[i - 1] < k:
                ans += arr[i] + arr[i - 1]
                i -= 2
            else:
                i -= 1

        return ans

# Subarray Frequency Count Queries
from bisect import bisect_left, bisect_right

class Solution:
    def freqInRange(self, arr, queries):
        # Step 1: Preprocess positions of each element
        pos = {}
        for i, val in enumerate(arr):
            if val not in pos:
                pos[val] = []
            pos[val].append(i)
        
        # Step 2: Answer queries
        result = []
        for l, r, x in queries:
            if x not in pos:
                result.append(0)
                continue
            
            indices = pos[x]
            # Find count of indices in [l, r]
            left = bisect_left(indices, l)
            right = bisect_right(indices, r)
            result.append(right - left)
        
        return result


# Lexicographically smallest after removing k

class Solution:
    def lexicographicallySmallest(self, s, k):
        n = len(s)

        # Check if n is power of 2
        if (n & (n - 1)) == 0:
            k //= 2
        else:
            k *= 2

        # If removal not possible
        if k >= n or n - k == 0:
            return -1

        stack = []
        for ch in s:
            while stack and k > 0 and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # Remove remaining k from end
        if k > 0:
            stack = stack[:-k]

        return "".join(stack)

# Non-Attacking Black and White Knights

class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        total = n * m * (n * m - 1)
        attacks = 0
        if n > 1 and m > 2:
            attacks += 4 * (n - 1) * (m - 2)
        if n > 2 and m > 1:
            attacks += 4 * (n - 2) * (m - 1)
        return total - attacks

# Finding Profession


class Solution:
    def profession(self, level, pos):
        # Count set bits in (pos - 1)
        flips = bin(pos - 1).count('1')

        # If flips are even → Engineer, else Doctor
        return "Engineer" if flips % 2 == 0 else "Doctor"

# Delete Nodes with Greater on Right
# Structure of linked list node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def compute(self, head):
        # Step 1: Reverse the list
        head = self.reverse(head)
        
        # Step 2: Traverse and delete nodes
        max_val = head.data
        curr = head
        while curr and curr.next:
            if curr.next.data < max_val:
                # delete the node
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_val = curr.data
        
        # Step 3: Reverse again to restore order
        head = self.reverse(head)
        return head


# Binary Searchable Count
class Solution:
    def binarySearchable(self, arr):
        n = len(arr)
        ans = 0

        for i in range(n):
            l, r = 0, n - 1
            ok = True

            while l <= r:
                mid = (l + r) // 2

                if mid == i:
                    break

                if mid < i:
                    if arr[mid] >= arr[i]:
                        ok = False
                        break
                    l = mid + 1
                else:
                    if arr[mid] <= arr[i]:
                        ok = False
                        break
                    r = mid - 1

            if ok:
                ans += 1

        return ans

# Equal Point in Brackets
class Solution:
    def findIndex(self, s: str) -> int:
        n = len(s)
        
        # Step 1: Count total closing brackets
        close_count = s.count(')')
        open_count = 0
        
        # Step 2: Traverse string
        for k in range(n + 1):  # include split at n
            if open_count == close_count:
                return k
            
            # Step 3: Update counters
            if k < n:
                if s[k] == '(':
                    open_count += 1
                else:
                    close_count -= 1
        
        return -1  # if no equal point found

# Check Repeated Substring with K Replacements


class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        # If length not divisible by k, impossible
        if len(s) % k != 0:
            return False

        # Split into chunks of size k
        chunks = [s[i:i+k] for i in range(0, len(s), k)]

        # Count frequency of each chunk
        from collections import Counter
        freq = Counter(chunks)

        # Find the most common chunk
        most_common_chunk, count = freq.most_common(1)[0]

        # Number of chunks that differ
        diff_chunks = len(chunks) - count

        # Valid if at most one chunk differs
        return diff_chunks <= 1

# Binary Strings with Equal Sum of Two Halves
MOD = 10**9 + 7

class Solution:
    def computeValue(self, n):
        # Precompute factorials up to 2n
        fact = [1] * (2*n + 1)
        for i in range(1, 2*n + 1):
            fact[i] = (fact[i-1] * i) % MOD
        
        # Fermat's Little Theorem for modular inverse
        def modinv(a):
            return pow(a, MOD-2, MOD)
        
        # nCr = fact[n] / (fact[r] * fact[n-r])
        numerator = fact[2*n]
        denominator = (fact[n] * fact[n]) % MOD
        return (numerator * modinv(denominator)) % MOD


# Exit Point in a Matrix
class Solution:
    def exitPoint(self, mat):
        n, m = len(mat), len(mat[0])
        
        # directions: right, down, left, up
        di, dj = 0, 1   # start moving right
        i, j = 0, 0
        
        while 0 <= i < n and 0 <= j < m:
            if mat[i][j] == 1:
                mat[i][j] = 0
                # turn right (clockwise)
                di, dj = dj, -di
            
            i += di
            j += dj
        
        # step back to last valid cell
        i -= di
        j -= dj
        
        return [i, j]

# Minimum Cost to Fill Given Weight


class Solution:
    def minimumCost(self, cost, w):
        # Initialize DP array
        dp = [float('inf')] * (w + 1)
        dp[0] = 0  # base case

        # Iterate over all packet sizes
        for i in range(len(cost)):
            if cost[i] == -1:  # skip unavailable packets
                continue
            packet_size = i + 1
            packet_cost = cost[i]

            # Update dp for all weights >= packet_size
            for x in range(packet_size, w + 1):
                if dp[x - packet_size] != float('inf'):
                    dp[x] = min(dp[x], dp[x - packet_size] + packet_cost)

        return -1 if dp[w] == float('inf') else dp[w]


# Cut rope to maximise product
class Solution:
    def maxProduct(self, n):
        # Base cases
        if n == 2:
            return 1
        if n == 3:
            return 2

        product = 1
        # Cut as many 3's as possible
        while n > 4:
            product *= 3
            n -= 3

        product *= n
        return product


# Coverage of all Zeros in a Binary Matrix
class Solution:
    def findCoverage(self, mat):
        n, m = len(mat), len(mat[0])
        total_coverage = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    coverage = 0

                    # Check left
                    for k in range(j-1, -1, -1):
                        if mat[i][k] == 1:
                            coverage += 1
                            break

                    # Check right
                    for k in range(j+1, m):
                        if mat[i][k] == 1:
                            coverage += 1
                            break

                    # Check up
                    for k in range(i-1, -1, -1):
                        if mat[k][j] == 1:
                            coverage += 1
                            break

                    # Check down
                    for k in range(i+1, n):
                        if mat[k][j] == 1:
                            coverage += 1
                            break

                    total_coverage += coverage

        return total_coverage

# Equalize All Prefix Sums


class Solution:
    def optimalArray(self, arr):
        n = len(arr)
        prefix_sum = [0] * n
        prefix_sum[0] = arr[0]

        # build prefix sums
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + arr[i]

        result = []
        for i in range(n):
            m = i // 2
            median = arr[m]

            # left side cost
            left_cost = median * (m+1) - prefix_sum[m]

            # right side cost
            right_cost = (prefix_sum[i] - prefix_sum[m]) - median * (i-m)

            result.append(left_cost + right_cost)

        return result

# Last Digit of a^b
class Solution:
    def getLastDigit(self, a, b):
        # Step 1: Get last digit of a
        last_digit = int(a[-1])
        
        # Step 2: Cycles of last digits
        cycles = {
            0: [0],
            1: [1],
            2: [2, 4, 8, 6],
            3: [3, 9, 7, 1],
            4: [4, 6],
            5: [5],
            6: [6],
            7: [7, 9, 3, 1],
            8: [8, 4, 2, 6],
            9: [9, 1]
        }
        
        cycle = cycles[last_digit]
        cycle_len = len(cycle)
        
        # Step 3: Handle b = "0"
        if b == "0":
            return 1 if a != "0" else 0
        
        # Step 4: Compute b mod cycle_len
        # Since b can be huge, compute modulo directly from string
        b_mod = 0
        for digit in b:
            b_mod = (b_mod * 10 + int(digit)) % cycle_len
        
        # Step 5: Adjust index (0 means last element in cycle)
        if b_mod == 0:
            return cycle[-1]
        else:
            return cycle[b_mod - 1]

# Choose and Swap
class Solution:
    def chooseSwap(self, s: str) -> str:
        # Step 1: Track first occurrence of each character
        first_occurrence = {}
        for i, ch in enumerate(s):
            if ch not in first_occurrence:
                first_occurrence[ch] = i

        # Step 2: Traverse string and check for possible beneficial swap
        for i, ch in enumerate(s):
            for smaller in sorted(first_occurrence.keys()):
                if smaller < ch and first_occurrence[smaller] > i:
                    # Step 3: Perform swap
                    s = list(s)
                    for j in range(len(s)):
                        if s[j] == ch:
                            s[j] = smaller
                        elif s[j] == smaller:
                            s[j] = ch
                    return "".join(s)
        return s


# Maximum Area Between Bars
class Solution:
    def maxArea(self, height):
        n = len(height)
        left, right = 0, n - 1
        max_area = 0

        while left < right:
            # width is number of bars between left and right
            width = right - left - 1
            # height is min of the two bars
            curr_area = min(height[left], height[right]) * width
            max_area = max(max_area, curr_area)

            # move the pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Rat Maze With Multiple Jumps


class Solution:

    def ratmaze(self, mat, i, j, ans):
        n = len(mat)

        ans[i][j] = 1

        if i == n - 1 and j == n - 1:
            return True

        for k in range(1, mat[i][j] + 1):

            if j + k < n and mat[i][j + k] != 0:
                if self.ratmaze(mat, i, j + k, ans):
                    return True

            if i + k < n and mat[i + k][j] != 0:
                if self.ratmaze(mat, i + k, j, ans):
                    return True

        ans[i][j] = 0
        mat[i][j] = 0

        return False

    def shortestDist(self, mat):
        n = len(mat)

        ans = [[0] * n for _ in range(n)]

        if mat[0][0] != 0:
            if self.ratmaze(mat, 0, 0, ans):
                return ans

        return [[-1]]

# Count Matching Subsequences


class Solution:
    def countWays(self, s1: str, s2: str) -> int:
        MOD = 10**9 + 7
        n, m = len(s1), len(s2)

        # DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base case: empty s2
        for i in range(n + 1):
            dp[i][0] = 1

        # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
                else:
                    dp[i][j] = dp[i-1][j] % MOD

        return dp[n][m]

# Ways to Tile the Floor


class Solution:
    def countWays(self, n, m):
        MOD = 10**9 + 7

        # Case 1: n < m → only horizontal tiling possible
        if n < m:
            return 1

        # Case 2: n == m → either all horizontal or all vertical
        if n == m:
            return 2

        # Case 3: n > m → use DP
        dp = [0] * (n+1)
        for i in range(m):
            dp[i] = 1
        dp[m] = 2

        for i in range(m+1, n+1):
            dp[i] = (dp[i-1] + dp[i-m]) % MOD

        return dp[n]
