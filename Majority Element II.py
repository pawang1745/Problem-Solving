class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n = len(arr)
        if n == 0:
            return []
        
        t = n // 3  
        v = {}  
        
        for a in arr:
            if a in v:
                v[a] += 1
            else:
                v[a] = 1
        
        res = [k for k, c in v.items() if c > t]
        
        return sorted(res)
