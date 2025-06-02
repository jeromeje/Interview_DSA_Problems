class Solution {
    public int removeElement(int[] nums, int val) {
      int initial = o;
      for (int i=0;i<nums.length;i++){
        if(nums[i] != val){
          nums[initial] = nums[i];
          inital +=1;
        }
        return inital;
    }
}
