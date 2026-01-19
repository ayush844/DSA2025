class Solution {
    public boolean find132pattern(int[] nums) {
        Stack<Integer> st = new Stack();    // always store max value i.e. nums[j]
        int third = Integer.MIN_VALUE;  // value at k, that is nums[k] is such that nums[i] < nums[k] < nums[j]
        
        for(int i = nums.length -1; i >= 0; i--){
            if(nums[i] < third){
                return true;
            }
            while(!st.isEmpty() && nums[i] > st.peek()){
                third = st.pop();
            }
            st.push(nums[i]);
        }

        return false;
    }
}