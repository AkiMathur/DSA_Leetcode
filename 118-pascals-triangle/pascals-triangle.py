class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = []
        for i in range(1,numRows+1):
            temp = []
            for j in range(i):
                temp.append(1)
            final.append(temp)

        for i in range(2,len(final)):
            for j in range(1,len(final[i])-1):
                final[i][j] = final[i-1][j-1] + final[i-1][j]
        return final

