class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            countS,countT ={},{}
            for i in s:
                if i not in countS:
                    countS[i]=1
                elif i in countS:
                    countS[i]+=1
            for i in  t:        
                if i not in countT:
                    countT[i]=1
                elif i in countT:
                    countT[i]+=1

            return countS==countT

        return False
    

        
