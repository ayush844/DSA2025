class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        List<int[]> merged = new ArrayList<>();
        int[] current = intervals[0];

        for (int i = 1; i < intervals.length; i++){
            if (intervals[i][0] <= current[1]){
                current[1] = Math.max(intervals[i][1], current[1]);
            }else{
                merged.add(current);
                current = intervals[i];
            }
        }
        merged.add(current);

        return merged.toArray(new int[merged.size()][]);
    }
}