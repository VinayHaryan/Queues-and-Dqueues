from collections import deque
def maxResult(nums,k):
    n = len(nums)
    deq =deque()
    deq.append(0)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = nums[i] + dp[deq[0]]     #Maximum Value in deque within that window
        if deq[0] < i - k + 1:
            deq.popleft()                #Check whether left bound is still accessible or not
        while deq and dp[deq[-1]] < dp[i]:         
            deq.pop()                   s #Update deque with current i'th element
        deq.append(i)
    return dp[-1]                        #Return total score


# Time Complexity: O(n)
# Space Complexity: O(n)
nums = [1,-1,-2,4,-7,3]
k = 2
print(maxResult(nums,k))



