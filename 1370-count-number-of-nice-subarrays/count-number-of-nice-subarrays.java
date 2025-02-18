class Solution {

public int atMostGoal2(int[] nums, int goal) {
    if(goal < 0){
        return 0;
    }
    int left = 0;
    int right = 0;
    int sum = 0;
    int count = 0;

    while (right < nums.length){
        sum += nums[right] % 2;
        while (sum > goal){
            sum = sum - nums[left] % 2;
            left++;
        }
        count = count + (right - left + 1);
        right++;
    }

    return count;
}

    public int numberOfSubarrays(int[] nums, int k) {
        return atMostGoal2(nums, k) - atMostGoal2(nums, k - 1);
    }
}