class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int nTotal = nums2.length;
        int totalNGE[] = new int[nTotal];
        int finalNGE[] = new int[n]; 
        Stack<Integer> st = new Stack<>();
        for (int i = nTotal - 1; i >= 0; i--){
            while (!st.isEmpty() && st.peek() <= nums2[i]){
                st.pop();
            }
            if (st.isEmpty()){
                totalNGE[i] = -1;
            }else {
                totalNGE[i] = st.peek();
            }
            st.push(nums2[i]);
        }
        
        for (int i = 0; i < n; i++){
            int element = nums1[i];
            for (int j = 0; j < nTotal; j++){
                if (element==nums2[j]){
                    finalNGE[i] = totalNGE[j];
                    break;
                }
            }
        }
        
        return finalNGE;
        
    }
}