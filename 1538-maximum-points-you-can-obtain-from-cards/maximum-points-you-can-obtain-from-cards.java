class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int lsum = 0;
        int rsum = 0;
        int maxScore = 0;
        int n = cardPoints.length;
        for (int i = 0; i < k; i++){
            lsum += cardPoints[i];
        }

        maxScore = lsum;
        int rightIndex = n-1;

        for (int i = k - 1; i>= 0; i--){
            lsum = lsum - cardPoints[i];
            rsum = rsum + cardPoints[rightIndex];
            rightIndex--;
            maxScore = Math.max(maxScore, lsum + rsum);
        }

        return maxScore;

    }
}