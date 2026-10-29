class Solution {
    HashMap<Integer,Integer> cache;
    public int minCostClimbingStairs(int[] cost) {
        cache = new HashMap<Integer,Integer>();
        return Math.min(dfs(cost, 0), dfs(cost, 1));
    }

    private int dfs(int[] cost, int i)
    {
        if(i >= cost.length)
        {
            return 0;
        }
        if(cache.containsKey(i))
        {
            return cache.get(i);
        }  
        cache.put(i,cost[i] + Math.min(dfs(cost, i + 1), dfs(cost, i + 2)));
        return cache.get(i);
    }
}
