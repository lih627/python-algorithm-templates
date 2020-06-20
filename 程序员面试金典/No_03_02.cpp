class MinStack {
    vector<int> stack;
    vector<int> minStack;
public:
    /** initialize your data structure here. */
    MinStack(){
        stack.clear();
        minStack.clear();
    }

    void push(int x) {
        stack.push_back(x);
        if (minStack.empty() || x <= minStack.back()) minStack.push_back(x);
    }

    void pop() {
        if (stack.empty()) return;
        if (stack.back() == minStack.back()){
            stack.pop_back();
            minStack.pop_back();
        }
        else stack.pop_back();
    }

    int top() {
        if (stack.empty()) return 0;
        return stack.back();
    }

    int getMin() {
        if (minStack.empty()) return 0;
        return minStack.back();

    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */