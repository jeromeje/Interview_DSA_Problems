# Question: 
## leetcode:26. Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
## Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
## Custom Judge:
## The judge will test your solution with the following code:
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length
int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

## Example 1:
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```
## Example 2:
```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 ```
Constraints:
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.


# ANSWER :

🔍 Explanation (Step-by-Step)
1. Two Pointers
> slow: Points to the last unique element.

> fast: Moves through the array, checking for new unique elements.

2. Logic
> Start slow at 0 and fast at 1.

> If nums[fast] != nums[slow], it means a new unique element is found:

> Move slow one step forward.

> Copy nums[fast] to nums[slow].

3. In-Place Update
> The first slow + 1 elements of the array will be the unique elements.

> No additional space is used.

logic:
```
1. slow be the first number              => slow = 0th index
2. for loop search from the 1 element    => fast = 1st index
3. if the the 0th and 1st element is same=> then slow add by 1 index and added index may have the non reapeated value


```
