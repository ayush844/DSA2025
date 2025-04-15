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
    public List<List<Integer>> verticalTraversal(TreeNode root) {
    // Map to store: vertical -> level -> list of node values (allows duplicates)
    Map<Integer, Map<Integer, List<Integer>>> nodes = new TreeMap<>();

    // Queue for BFS traversal: each item is (node, (vertical, level))
    Queue<Pair<TreeNode, Pair<Integer, Integer>>> todo = new LinkedList<>();
    todo.add(new Pair<>(root, new Pair<>(0, 0)));

    // BFS traversal
    while (!todo.isEmpty()) {
        Pair<TreeNode, Pair<Integer, Integer>> p = todo.poll();
        TreeNode temp = p.getKey();
        int x = p.getValue().getKey();   // vertical
        int y = p.getValue().getValue(); // level

        // Add node value to the map
        nodes
            .computeIfAbsent(x, k -> new TreeMap<>())
            .computeIfAbsent(y, k -> new ArrayList<>())
            .add(temp.val); // Use List to allow duplicates

        // Left child: vertical - 1, level + 1
        if (temp.left != null) {
            todo.add(new Pair<>(temp.left, new Pair<>(x - 1, y + 1)));
        }

        // Right child: vertical + 1, level + 1
        if (temp.right != null) {
            todo.add(new Pair<>(temp.right, new Pair<>(x + 1, y + 1)));
        }
    }

    // Prepare the final result
    List<List<Integer>> ans = new ArrayList<>();
    for (Map<Integer, List<Integer>> levelMap : nodes.values()) {
        List<Integer> col = new ArrayList<>();
        for (List<Integer> values : levelMap.values()) {
            Collections.sort(values); // Sort manually to maintain required order
            col.addAll(values);
        }
        ans.add(col);
    }

    return ans;
}

}