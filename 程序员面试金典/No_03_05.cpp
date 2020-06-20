class SortedStack {
    stack<int> s;
public:
    SortedStack() {

    }

    void push(int val) {
        if(s.empty()) {s.push(val);return;}
        stack<int> tmp;
        while(!s.empty() && val > s.top()){
            tmp.push(s.top());
            s.pop();
        }
        s.push(val);
        while(!tmp.empty()){
            s.push(tmp.top());
            tmp.pop();
        }
    }

    void pop() {
        if(!s.empty()) s.pop();
    }

    int peek() {
        if(!s.empty()) return s.top();
        return -1;
    }

    bool isEmpty() {
        return s.empty();

    }
};

/**
 * Your SortedStack object will be instantiated and called as such:
 * SortedStack* obj = new SortedStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->isEmpty();
 */