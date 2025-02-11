class Solution {

    public int largestRectangleArea2(int[] heights) {
        int len = heights.length; // Get the number of bars in the histogram
        Stack<Integer> st = new Stack<>(); // Stack to store indices of the histogram bars
        int maxArea = 0; // Variable to track the maximum area encountered

        // Iterate through the histogram, including a virtual bar of height 0 at the end
        for (int i = 0; i <= len; i++) {
            // For the virtual bar at the end, height is 0. Otherwise, take the current bar height.
            int h = (i == len) ? 0 : heights[i];

            // If the stack is empty or the current height is greater than or equal to the height at the top of the stack:
            if (st.isEmpty() || h >= heights[st.peek()]) {
                st.push(i); // Push the current index onto the stack
            } else {
                // When the current height is less than the height of the bar at the top of the stack:
                int tp = st.pop(); // Pop the top index from the stack
                // Calculate the width of the rectangle with the popped bar as the smallest (height-defining) bar:
                int width = st.isEmpty() ? i : i - 1 - st.peek(); // If the stack is empty, the rectangle extends from 0 to `i - 1`
                // Calculate the area of the rectangle using the popped bar as height and the computed width
                maxArea = Math.max(maxArea, heights[tp] * width);
                i--; // Decrement `i` to re-evaluate the current bar with the new stack top
            }
        }

        return maxArea; // Return the maximum area found
    }


    public int maximalRectangle(char[][] matrix) {
        // Edge case: If matrix is empty
    if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
        return 0;
    }

    int n = matrix.length; // Number of rows
    int m = matrix[0].length; // Number of columns

    int[] heights = new int[m]; // Histogram heights for each column
    int maxArea = 0; // Track the maximum rectangle area

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // Update histogram heights: Increment for '1', reset to 0 for '0'
            if (matrix[i][j] == '1') {
                heights[j]++; // Increment height for column `j`
            } else {
                heights[j] = 0; // Reset height for column `j` if '0' is encountered
            }
        }

        // Calculate the largest rectangle area for the current histogram
        maxArea = Math.max(maxArea, largestRectangleArea2(heights));
    }

    return maxArea; 
    }
}