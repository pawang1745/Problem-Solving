class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here

        citations.sort(reverse=True)
        hindex = 0
        
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                hindex = i + 1
            else:
                break
        
        return hindex
