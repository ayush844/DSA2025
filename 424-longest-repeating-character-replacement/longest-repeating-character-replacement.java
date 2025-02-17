class Solution {
    public int characterReplacement(String s, int k) {
        
        int start = 0;
        int maxCount = 0;
        int maxLen = 0;
        int[] count = new int[26];

        for (int end = 0; end < s.length(); end++){
            maxCount = Math.max(maxCount, ++count[s.charAt(end) - 'A']);
            while (end - start + 1 - maxCount > k){
                count[s.charAt(start) - 'A']--;
                start++;
            }
            maxLen = Math.max(maxLen, end - start + 1);
        }
        
        return maxLen;
    }
}