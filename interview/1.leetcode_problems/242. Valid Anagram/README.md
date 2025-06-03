# Q. leetcode 242. same words in two strings: 
# A. 
## Type1: change the two string to sorted and compare to get ans
## Type2: dict: add the elements in dictiory with their occurance and compare it.
## Type3: Hashing 

> step1:
return false if length of two string is not equal
```
if len(s)!= len(t)
return False
```
>step2:
initial two dictinary for two string:
```
countS,countT ={},{}
```
>step3:
Iterate each element in the string and add to the string if not exist then string[] = 1
if it exist then string[] +=1 in dictnary
```
for i in s:
   if i not in countS:
       countS[i]=1
   elif i in countS:
       countS[i]+=1
```
step4:
compare them and give output 
