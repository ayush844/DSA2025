class Solution {
    public boolean canJump(int[] nums) {
        int maxTotal = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++){
            if (i > maxTotal){
                return false;
            }

            maxTotal = Math.max(maxTotal, i + nums[i]);

        }

        return true;
    }
}