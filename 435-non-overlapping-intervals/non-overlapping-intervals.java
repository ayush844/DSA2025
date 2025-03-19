class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
        int n = intervals.length;
        int cnt = 1;    // we'll take the first meeting
        int lastEndingTime = intervals[0][1];   // ending time of first meeting

        for (int i = 0; i < n; i++){
            if(intervals[i][0] >= lastEndingTime){
                lastEndingTime = intervals[i][1];
                cnt++;
            }
        }
        
        return n - cnt;
    }
}