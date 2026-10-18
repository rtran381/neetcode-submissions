class Solution {
    public int maxProfit(int[] prices) {
        int buy = prices[0];
        int profit = 0;

        for(int s: prices)
        {
            profit = Math.max(profit, s - buy);
            buy = Math.min(buy,s);
        }
        return profit;
    }
}
