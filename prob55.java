//Time complexity- O[N]
//Space complexity-O[1]
//Ran successfully in leetcode
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        //Base case
        List<Integer> result= new ArrayList<>();
        helper(root,0,result);
        return result;
    }
    
    private void helper(TreeNode root,int d,List result){
        //base case
        if(root==null) return;
        if(d==result.size()) result.add(root.val);
        if(root.right!=null)
            helper(root.right,d+1,result);
        if(root.left!=null)
            helper(root.left,d+1,result);
    }
}