class Solution:
    def pushZerosToEnd(self,arr):
        # code here
        j=0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i],arr[j] = arr[j],arr[i]
                j += 1
