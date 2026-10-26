class KthLargest {
    private int k;
    private  PriorityQueue<Integer> min;


    public KthLargest(int k, int[] nums) {
        this.k = k;
        min = new PriorityQueue<Integer>();
        for(int num : nums)
        {
            min.add(num);
            if(min.size() > k)
            {
                min.poll();
            }
        }
        
    }
    
    public int add(int val) {
        min.add(val);
        if(min.size() > k)
        {
            min.poll();
        }
        return min.peek();
    }
}
