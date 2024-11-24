class Solution:
    def maxSubArraySum(self,arr):
        max_sum = float('-inf') 
        current_sum = 0
        
        for num in arr:
            current_sum += num
            if current_sum < num:
                current_sum = num  
            max_sum = max(max_sum, current_sum)
        
        return max_sum
