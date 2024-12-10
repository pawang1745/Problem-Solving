class Solution:
    def minRemoval(self, intervals):
        # Code here
        cnt = 0
    
        intervals.sort(key=lambda x: x[1])
    
        end = intervals[0][1]
    
        for i in range(1, len(intervals)):
    
            if intervals[i][0] < end:
                cnt += 1
    
            # else increment the ending point
            else:
                end = intervals[i][1]
    
        return cnt