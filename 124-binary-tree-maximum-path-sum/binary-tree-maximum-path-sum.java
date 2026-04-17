/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    int max_sum = Integer.MIN_VALUE;

    public int maxGain(TreeNode node){
        if(node == null){
            return 0;
        }

        int leftGain  = Math.max(maxGain(node.left), 0);
        int rightGain  = Math.max(maxGain(node.right), 0);

        int pathSum = node.val + leftGain + rightGain;
        max_sum = Math.max(max_sum, pathSum);

        return node.val + Math.max(leftGain, rightGain);

    }

    public int maxPathSum(TreeNode root) {
        maxGain(root);
        return max_sum;
    }
}