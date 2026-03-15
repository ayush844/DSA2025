class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> st = new Stack<>();

        for(String tk: tokens){
            if(isOperator(tk)){
                int b = st.pop();
                int a = st.pop();
                st.push(applyOperator(tk, a, b));
            }else{
                st.push(Integer.parseInt(tk));
            }
        }

        return st.pop();
    }

    public boolean isOperator(String token){
        return token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/");
    }

    public int applyOperator(String operator, int a, int b){
        if(operator.equals("+")){
            return a + b;
        }else if(operator.equals("-")){
            return a - b;
        }else if(operator.equals("*")){
            return a * b;
        }else if(operator.equals("/")){
            return a / b;
        }
        return 0;
    }
}