class Solution {
    public boolean checkValidString(String s) {
        // for '(' add 1, for ')' add -1 and for empty add 0
        int cmin = 0;
        int cmax = 0;

        for (char c : s.toCharArray()){
            if (c == '('){
                cmax++;
                cmin++;
            } else if (c == ')') {
                cmax--;
                cmin--;
            } else if (c == '*') {
                cmax++;
                cmin--;
            }

            if (cmax < 0) return false;

            cmin = Math.max(cmin, 0);
        }

        return cmin == 0;
    }
}