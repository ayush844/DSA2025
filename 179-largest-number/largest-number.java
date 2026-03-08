class Solution {
    public String largestNumber(int[] nums) {
        String[] asString = new String[nums.length];

        for(int i = 0; i < nums.length; i++){
            asString[i] = String.valueOf(nums[i]);
        }

        // Arrays.sort(asString, new Comparator<String>(){
        //     public int compare(String a, String b){
        //         String order1 = a + b;
        //         String order2 = b + a;
        //         return order1.compareTo(order2);
        //     }
        // });
        Arrays.sort(asString, (a,b) -> (b+a).compareTo(a+b));

        if(asString[0].equals("0")){
            return "0";
        }

        StringBuilder largestNum = new StringBuilder();

        for(String numAsStr : asString){
            largestNum.append(numAsStr);
        }

        return largestNum.toString();

    }
}