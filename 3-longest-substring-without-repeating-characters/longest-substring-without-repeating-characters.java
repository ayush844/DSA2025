class Solution {
    public int lengthOfLongestSubstring(String s) {
    if (s.isEmpty()) {
        return 0;
    }

    int maxans = 0;  // Start from 0 instead of Integer.MIN_VALUE

    for (int i = 0; i < s.length(); i++) {
        Set<Character> se = new HashSet<>();
        for (int j = i; j < s.length(); j++) {
            if (se.contains(s.charAt(j))) {
                break;  // Break if a duplicate is found
            }
            se.add(s.charAt(j));
            maxans = Math.max(maxans, j - i + 1); // Update maxans for every valid substring
        }
    }

    return maxans;

    }
}