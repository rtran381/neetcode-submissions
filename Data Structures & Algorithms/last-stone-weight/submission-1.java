class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> s = new PriorityQueue<Integer>(Collections.reverseOrder());
        for(int stone : stones)
        {
            s.add(stone);
        }
        System.out.println(s);

        while(s.size() > 1)
        {
            int s1 = s.poll();
            int s2 = s.poll();

            if(s1 > s2)
            {
                s.add(s1 - s2);
            }
        }

        s.add(0);
        return s.peek();
    }
}
