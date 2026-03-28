class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if(nums == null || nums.length == 0 || k <= 0){
            return new int[0];
        }

        int n = nums.length;
        int[] result = new int[n-k+1];
        Deque<Integer> dq = new LinkedList<>();

        for(int i = 0; i < n; i++){
            // // remove indices that are out of our window
            // while(!dq.isEmpty() && (dq.peek() < (i - k + 1))){
            //     dq.poll();
            // }
            
            // // remove indices whose corresponding vlues are less than nums[i]
            // while(!dq.isEmpty() && nums[dq.peekLast()] < nums[i]){
            //     dq.pollLast();
            // }

            // // add current index to deque
            // dq.offer(i);

            // if(i >= k-1){
            //     result[i-k+1] = nums[dq.peek()];
            // }







            while(!dq.isEmpty() && dq.peek() < i-k+1){
                dq.poll();
            }

            while(!dq.isEmpty() && nums[dq.peekLast()] < nums[i]){
                dq.pollLast();
            }

            dq.offer(i);

            if(i >= k-1){
                result[i-k+1] = nums[dq.peek()];
            }
        }

        return result;

    }
}