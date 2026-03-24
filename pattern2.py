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