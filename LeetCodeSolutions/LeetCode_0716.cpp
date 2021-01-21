class MaxStack {
    list<int> stk;
    map<int, vector<list<int>::iterator>> mp;
public:
    /** initialize your data structure here. */
    MaxStack() :stk(),mp() {
    }

    void push(int x) {
        stk.push_back(x);
        mp[x].push_back(--stk.end());
    }

    int pop() {
        int ret = stk.back();
        mp[ret].pop_back();
        if (mp[ret].empty()) mp.erase(ret);
        stk.pop_back();
        return ret;
    }

    int top() {
        return stk.back();
    }

    int peekMax() {
        return (*mp.rbegin()).first;
    }

    int popMax() {
        int m = (*mp.rbegin()).first;
        auto it = mp[m].back();
        mp[m].pop_back();
        if(mp[m].empty()) mp.erase(m);
        stk.erase(it);
        return m;
    }
};

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack* obj = new MaxStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->peekMax();
 * int param_5 = obj->popMax();
 */