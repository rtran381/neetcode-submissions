class Solution {
    public boolean hasDuplicate(int[] nums) 
    {
        HashSet<Integer> s = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++)
        {
            s.add(nums[i]);
        }
        return nums.length != s.size();
    }
}