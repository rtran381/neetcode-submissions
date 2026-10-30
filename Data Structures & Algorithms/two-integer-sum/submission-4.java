class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(var i = 0; i <= nums.length; i++)
        {
            int diff = target - nums[i];
            if(map.containsKey(diff))
            {
                int[] res = {map.get(diff), i};
                return res;
            }
            map.put(nums[i],i);
        }
        return null;
    }
}
