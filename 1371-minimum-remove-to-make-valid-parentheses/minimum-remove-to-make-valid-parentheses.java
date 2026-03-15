class Solution {
    public String minRemoveToMakeValid(String s) {
        Set<Integer> removeIndices = new HashSet<>();
        Stack<Integer> st = new Stack<>();

        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '('){
                st.push(i);
            }else if (s.charAt(i) == ')'){
                if(st.isEmpty()){
                    removeIndices.add(i);
                }else{
                    st.pop();
                }
            }
        }

        while(!st.isEmpty()){
            removeIndices.add(st.pop());
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            if(!removeIndices.contains(i)){
                sb.append(s.charAt(i));
            }
        }

        return sb.toString();
    }
}