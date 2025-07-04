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


    class BSTIterator2 {

        private Stack<TreeNode> stack = new Stack<>();
        boolean reverse = true;

        public BSTIterator2(TreeNode root, boolean isReverse) {
            reverse = isReverse;
            pushAll(root);
        }

        public boolean hasNext() {
            return !stack.isEmpty();
        }


        public int next() {
            TreeNode temp = stack.pop();

            if (reverse == false){
                pushAll(temp.right);
            }else {
                pushAll(temp.left);
            }

            return temp.val;
        }


        private void pushAll(TreeNode node){
             while (node != null) {
                 stack.push(node);
                 if (reverse == true){
                     node = node.right;
                 }else {
                     node = node.left;
                 }
             }
        }
    }


class Solution {
    public boolean findTarget(TreeNode root, int k) {
        if (root == null){
            return false;
        }

        BSTIterator2 l = new BSTIterator2(root, false);
        BSTIterator2 r = new BSTIterator2(root, true);

        int i = l.next();
        int j = r.next();

        while (i < j){
            if (i + j == k){
                return true;
            } else if (i + j < k) {
                i = l.next();
            } else {
                j = r.next();
            }
        }

        return false;

    }
}