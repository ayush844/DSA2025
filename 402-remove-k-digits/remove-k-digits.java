class Solution {
    public String removeKdigits(String num, int k) {
        
        int len = num.length();

        if (len == k){
            return "0";
        }

        Stack<Character> st = new Stack<>();

        int i = 0;

        while (i < num.length()){
            while (k > 0 && !st.isEmpty() && st.peek() > num.charAt(i)){
                st.pop();
                k--;
            }

            st.push(num.charAt(i));
            i++;
        }

        // corner case like "1111" or "123456"
        while (k > 0){
            st.pop();
            k--;
        }

        //construct the number from the stack
        StringBuilder sb = new StringBuilder();
        while(!st.isEmpty())
            sb.append(st.pop());
        sb.reverse();

        //remove all the 0 at the head
        while(sb.length()>1 && sb.charAt(0)=='0')
            sb.deleteCharAt(0);
        return sb.toString();

    }
}