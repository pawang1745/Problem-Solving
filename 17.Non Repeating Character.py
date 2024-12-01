class Solution:
    
    def nonRepeatingChar(self,s):
       #code here
        MAX_CHAR = 26
        vis = [-1] * MAX_CHAR
    
        for i in range(len(s)):
    
            if vis[ord(s[i]) - ord('a')] == -1:
                vis[ord(s[i]) - ord('a')] = i
            else:
                vis[ord(s[i]) - ord('a')] = -2
    
        idx = float('inf')
    
        for i in range(MAX_CHAR):
            if vis[i] >= 0:
                idx = min(idx, vis[i])
    
        return '$' if idx == float('inf') else s[idx]
