class Solution {

public int[] findNSE(int[] arr) {
        int n = arr.length;
        int[] nse = new int[n];

        // Stack to store indexes
        Stack<Integer> st = new Stack<>();

        for (int i = n - 1; i >= 0; i--) {
            while (!st.isEmpty() && arr[st.peek()] >= arr[i]) {
                st.pop();
            }
            nse[i] = st.isEmpty() ? n : st.peek();
            st.push(i);
        }

        return nse;
    }

    // Finding Previous Smaller Element Equal or Less Than
    public int[] findPSEE(int[] arr) {
        int n = arr.length;
        int[] psee = new int[n];

        // Stack to store indexes
        Stack<Integer> st = new Stack<>();

        for (int i = 0; i < n; i++) {
            while (!st.isEmpty() && arr[st.peek()] > arr[i]) {
                st.pop();
            }
            psee[i] = st.isEmpty() ? -1 : st.peek();
            st.push(i);
        }

        return psee;
    }

    public int sumSubarrayMins(int[] arr) {
        int[] nse = findNSE(arr);
        int[] psee = findPSEE(arr);

        int total = 0;
        int mod = (int) (1e9 + 7);

        for (int i = 0; i < arr.length; i++) {
            int left = i - psee[i];
            int right = nse[i] - i;

            total = (int) ((total + (arr[i] * 1L * left * right) % mod) % mod);
        }

        return total;
    }
}