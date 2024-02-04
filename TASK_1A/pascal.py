class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        from math import comb
        ans=[]
        for i in range(numRows):
            col=[0]*(i+1)
            for _ in range(i+1):
                col[]=comb(i,)
            ans.append(col)
        
        return ans