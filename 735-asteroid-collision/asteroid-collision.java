class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> s = new Stack<>();
        for (int i: asteroids){
            if(i > 0){
                s.push(i);
            }else{
                while (!s.isEmpty() && s.peek() > 0 && s.peek() < Math.abs(i)){
                    s.pop();
                }
                if (s.empty() || s.peek() < 0){
                    s.push(i);
                }else if (i + s.peek() == 0){
                    s.pop();
                }
            }
        }

        int[] res = new int[s.size()];

        for (int i = res.length-1; i >= 0; i--){
            res[i] = s.pop();
        }
        
        return res;
    }
}