class Solution:
	def maxProduct(self,arr):
        if not arr:
            return 0
    
        max_so_far = arr[0]
        min_so_far = arr[0]
        result = arr[0]
    
        for i in range(1, len(arr)):
            if arr[i] < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            
            max_so_far = max(arr[i], arr[i] * max_so_far)
            min_so_far = min(arr[i], arr[i] * min_so_far)
    
            result = max(result, max_so_far)
    
        return result
