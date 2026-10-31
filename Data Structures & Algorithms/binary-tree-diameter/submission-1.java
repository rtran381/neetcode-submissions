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
    public int diameterOfBinaryTree(TreeNode root) {
        if(root == null)
        {
            return 0;
        }
        int d = dfs(root.left, 0) + dfs(root.right, 0);
        return Math.max(Math.max(d, diameterOfBinaryTree(root.left)),diameterOfBinaryTree(root.right));
    }

    private int dfs(TreeNode node, int h)
    {
        if(node == null)
        {
            return h;
        }
        return Math.max(dfs(node.left, h + 1), dfs(node.right, h + 1));
    }
}
