class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        size_of_needle= len(needle)
        if needle == haystack:
            return 0
        for i in range (0,len(haystack)-len(needle)+1):
            if (haystack[start:size_of_needle] != needle):
                start +=1
                size_of_needle +=1
            else: 
                return i
        return -1
