class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        f_max = 0
        s_max = 0
        
        for i in arr:
            if(i > f_max):
                f_max = i
                
        for i in arr:
            if(i < f_max and i > s_max):
                s_max = i
                
        if(s_max == 0):
            return -1
        else:
            return s_max
