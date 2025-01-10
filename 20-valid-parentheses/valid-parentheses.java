class Solution {
    public boolean isValid(String s) {
                // since we have to know the last opening, we need to store all the openings, and since we are getting the last entered opening we will use stack

                Stack<Character> charStack = new Stack<Character>();

                for(char i : s.toCharArray()){
                    if(i == '(' || i == '{' || i == '['){
                        charStack.push(i);
                    }else{
                        if(charStack.isEmpty()) return false;   // it doesn't have closing bracket
                        char ch = charStack.pop();
                        if((ch == '(' && i == ')') || (ch == '{' && i == '}') || (ch == '[' && i == ']')){
                            continue;
                        }else{
                            return false;
                        }
                    }
                }

                if(charStack.isEmpty()){
                    return true;
                }else{
                    return false;
                }

            
    }
}