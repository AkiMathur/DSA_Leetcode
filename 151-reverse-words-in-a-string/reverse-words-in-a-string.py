class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        s = ""
        for i in range(len(words)-1, -1, -1):
            if i == 0:
                s += words[i]
            else:    
                s += words[i] + " "
        return s