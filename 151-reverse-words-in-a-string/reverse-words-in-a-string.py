class Solution:
    def reverseWords(self, s: str) -> str:
        l_w = len(s)
        end = len(s)
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                if i == 0 or s[i-1] == " ":
                    s += s[i:end] + " "
            else:
                end = i
                
        s = s[l_w:len(s)-1] 
        return s