# 🧠 LeetCode 5 - Longest Palindromic Substring (Optimized - Manacher's Algorithm)

## 🚀 Problem Statement

Given a string `s`, return the **longest palindromic substring** in `s`.

> A string is a palindrome if it reads the same backward as forward.

### ✅ Example:
```text
Input: "babad"
Output: "bab"  // "aba" is also valid
 ```


## 🧾  Answer:

🪜 Step-by-Step Explanation
## 🔹 Step 1: Define the Expansion Function:
```
def expandAroundCenter(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]
```
---This helper function expands the pointers outward (left--, right++) as long as:
> 1. We stay within bounds.
> 2. Characters on both ends match (s[left] == s[right]).
> 3. It returns the longest palindrome for a given center.

## 🔹 Step 2: Loop Through Each Character in the String:
```
for i in range(len(s)):
```
> 1. We consider each character in the string as a potential center of a palindrome.

## 🔹 Step 3: Check for Odd-Length and Even-Length Palindromes
```
temp1 = expandAroundCenter(i, i)       # Odd length (like "aba")
temp2 = expandAroundCenter(i, i + 1)   # Even length (like "abba")
```
   --- We check both possibilities:
> 1.  i , i for odd-length palindromes.
> 2.  i , i+1 for even-length palindromes.

## 🔹 Step 4: Update the Longest Palindrome Found
```
if len(temp1) > len(longest):
    longest = temp1
if len(temp2) > len(longest):
    longest = temp2
```
> We update the longest variable if a longer palindrome is found.

🔹 Step 5: Return the Result
```
return longest
```
> Finally, return the longest palindromic substring found.

🧪 Example
```
Input: "babad"
Output: "bab" or "aba"
```
> Both "bab" and "aba" are valid palindromes of length 3.
