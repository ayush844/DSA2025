/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {



    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {

        if(root == null){
            return "";
        }

        StringBuilder sb = new StringBuilder();

        Queue<TreeNode> q = new LinkedList<>();

        q.add(root);

        while (!q.isEmpty()){
            TreeNode currNode = q.poll();

            if(currNode == null){
                sb.append("#,");
            }else{
                sb.append(currNode.val).append(",");

                q.add(currNode.left);
                q.add(currNode.right);
            }

        }

        return sb.toString();

    }

    // Decodes your encoded data to tree.
public TreeNode deserialize(String data) {
    if (data.isEmpty()) {
        return null;
    }

    StringBuilder s = new StringBuilder(data);

    int commaIndex = s.indexOf(",");
    String str = s.substring(0, commaIndex);
    s.delete(0, commaIndex + 1);

    TreeNode root = new TreeNode(Integer.parseInt(str));
    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);

    while (!q.isEmpty()) {
        TreeNode node = q.poll();

        // Parse left node
        commaIndex = s.indexOf(",");
        if (commaIndex == -1) break;
        str = s.substring(0, commaIndex);
        s.delete(0, commaIndex + 1);

        if (!str.equals("#")) {
            TreeNode leftNode = new TreeNode(Integer.parseInt(str));
            node.left = leftNode;
            q.offer(leftNode);
        }

        // Parse right node
        commaIndex = s.indexOf(",");
        if (commaIndex == -1) break;
        str = s.substring(0, commaIndex);
        s.delete(0, commaIndex + 1);

        if (!str.equals("#")) {
            TreeNode rightNode = new TreeNode(Integer.parseInt(str));
            node.right = rightNode;
            q.offer(rightNode);
        }
    }

    return root;
}


}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));