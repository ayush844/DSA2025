class Solution {
    public String largestNumber(int[] nums) {
        String[] asStr = new String[nums.length];

        for(int i = 0; i < nums.length; i++){
            asStr[i] = String.valueOf(nums[i]);
        }

        Arrays.sort(asStr, (a, b) -> (b + a).compareTo(a + b));

        if(asStr[0].equals("0")){
            return "0";
        }

        StringBuilder largestNum = new StringBuilder();

        for(String numAsStr : asStr){
            largestNum.append(numAsStr);
        }

        return largestNum.toString();
    }
}