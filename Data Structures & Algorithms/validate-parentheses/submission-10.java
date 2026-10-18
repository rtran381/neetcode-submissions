class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        HashMap<Character, Character> m = new HashMap<Character, Character>();
        m.put(']', '[');
        m.put('}', '{');
        m.put(')', '(');

        for(int i = 0; i < s.length(); i++)
        {
            if(m.containsKey(s.charAt(i)) && ! stack.isEmpty())
            {
                char var = stack.pop();
                if(var != m.get(s.charAt(i)))
                {
                    return false;
                }
            }
            else
            {
                stack.push(s.charAt(i));                
            }
        }
        
        if(stack.isEmpty())
        {
            return true;
        }
        return false;
    }
}
