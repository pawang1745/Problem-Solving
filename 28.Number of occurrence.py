class Solution:
    def countFreq(self, arr, target):
        #code here
        count = 0
        for i in arr:
            if i == target:
                count+=1
                
        return count
