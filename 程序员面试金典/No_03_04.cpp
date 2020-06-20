class MyQueue {
    stack<int> iStack, oStack;
public:
    /** Initialize your data structure here. */
    MyQueue() {

    }

    /** Push element x to the back of queue. */
    void push(int x) {
        iStack.push(x);
    }
    void _trans(){
        if(oStack.empty()){
            while(!iStack.empty()){
                oStack.push(iStack.top());
                iStack.pop();
            }
    }
    }
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        _trans();
        if(!oStack.empty()){
            int ans = oStack.top();
            oStack.pop();
            return ans;
        }
        else return -1;

    }

    /** Get the front element. */
    int peek() {
        _trans();
        if(!oStack.empty()) return oStack.top();
        else return -1;

    }

    /** Returns whether the queue is empty. */
    bool empty() {
        return iStack.empty() && oStack.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */