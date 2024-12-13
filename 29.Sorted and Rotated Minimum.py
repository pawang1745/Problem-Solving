class Solution:
    def findMin(self, arr):
        min_ = arr[0] 
        for i in arr:
            min_ = min(min_, i)
        return min_
