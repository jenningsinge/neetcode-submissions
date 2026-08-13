class MinStack {

    private List<Integer> stack;

    private List<Integer> minElStack;

    public MinStack() {
        stack = new ArrayList<Integer>();
        minElStack = new ArrayList<Integer>();
    }
    
    public void push(int val) {
        if (stack.size() == 0 || val <= minElStack.get(minElStack.size()-1)) {
            minElStack.add(val);
        }
        stack.add(val);
    }
    
    public void pop() {
        Integer val = stack.remove(stack.size()-1);
        if (val.equals(minElStack.get(minElStack.size()-1))) {
            System.out.println(val);
            minElStack.remove(minElStack.size()-1);
        }
    }
    
    public int top() {
        return stack.get(stack.size()-1);
    }
    
    public int getMin() {
        return minElStack.get(minElStack.size()-1);
    }
}
