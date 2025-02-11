class Solution {
    public int largestRectangleArea(int[] heights) {
        
        int len = heights.length;
        Stack<Integer> st = new Stack<>();
        int maxArea = 0;

        for (int i = 0; i<= len; i++){
            int h = (i == len) ? 0 : heights[i];

            if(st.isEmpty() || h >= heights[st.peek()]){
                st.push(i);
            }else{
                int tp = st.pop();
                maxArea = Math.max(maxArea, heights[tp] * (st.isEmpty() ? i : i - 1 - st.peek()));
                i--;
            }
        }
        
        return maxArea;
    }
}