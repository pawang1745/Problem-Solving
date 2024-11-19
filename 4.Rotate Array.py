class Solution:
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d = d % n
        
        arr.reverse()
        arr[:n - d] = reversed(arr[:n - d])
        arr[n - d:] = reversed(arr[n - d:])
        return arr
