class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i in range(len(citations)):
            if (i+1 > citations[i]):
                return h
            else:
                h += 1
        return h