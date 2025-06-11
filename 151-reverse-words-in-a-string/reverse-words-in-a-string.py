class Solution:
    def reverseWords(self, s: str) -> str:
        l_w = len(s)
        strt,end = len(s)-1,len(s)
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                strt = i
                if strt == 0 or s[strt-1] == " ":
                    s += s[strt:end] + " "
            else:
                strt,end = i,i
                
        s = s[l_w:len(s)-1] 
        return s