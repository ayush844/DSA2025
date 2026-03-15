class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> mappedBrackets = new HashMap<>();
        Stack<Character> st = new Stack<>();

        mappedBrackets.put(')', '(');
        mappedBrackets.put('}', '{');
        mappedBrackets.put(']', '[');

        for(int i = 0; i < s.length(); i++){
            if(!mappedBrackets.containsKey(s.charAt(i))){
                st.push(s.charAt(i));
            }else{
                if(st.isEmpty()){
                    return false;
                }else{
                    char top = st.pop();
                    if(top != mappedBrackets.get(s.charAt(i))){
                        return false;
                    }
                }
            }
        }

        if(st.isEmpty()){
            return true;
        }else{
            return false;
        }
    }
}