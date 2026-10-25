class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        Arrays.sort(piles);
        int l = 1;
        int r = piles[piles.length - 1];
        int res = r;

        while(l <= r)
        {
            int m = (l + r) / 2;
            int time = 0;
            for(double p: piles)
            {
                time += Math.ceil(p / m);
            }
            if(time <= h)
            {
                res = m;
                r = m - 1;
            }
            else
            {
                l = m + 1;
            }
        }
        return res;
    }
}
