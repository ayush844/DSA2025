class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int right = 0;
        int n = nums.length;
        int maxLen = 0;
        int zeroes = 0;
        while (right < n){
            if(nums[right] == 0){
                zeroes ++;
            }

            while (zeroes > k){
                if(nums[left] == 0){
                        zeroes--;
                }
                left++;
            }
            
            maxLen = Math.max(right-left+1, maxLen);
            right++;
        }

        return maxLen;
    }
}