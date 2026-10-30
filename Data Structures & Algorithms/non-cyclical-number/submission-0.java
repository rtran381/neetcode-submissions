class Solution {
    HashSet<Integer> set;
    public boolean isHappy(int n) {
        set = new HashSet<>();
        while(n != 1)
        {
            set.add(n);
            n = sum(n);
            if(set.contains(n))
            {
                return false;
            }
        }
        return true;
    }

    private int sum(int n)
    {
        int s = 0;
        while(n > 0)
        {
            int digit = n % 10;
            n = n / 10;
            s += digit * digit;
        }
        s += n * n;
        return s;
    }
}
