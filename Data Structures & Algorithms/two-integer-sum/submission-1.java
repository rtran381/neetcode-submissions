class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> d = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++)
        {
            int diff = target - nums[i];
            if(d.containsKey(diff))
            {
                int[] ret = {d.get(diff), i};
                System.out.print(ret);
                return ret;
            }
            else
            {
                d.put(nums[i], i);
            }

        }
        return null;
    }
}
