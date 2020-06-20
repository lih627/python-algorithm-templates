class StackOfPlates {
    list<stack<int> > ls;
    int sz;
public:
    StackOfPlates(int cap) {
       sz = cap;
    }

    void push(int val) {
        if(sz == 0)return;
        if(!ls.empty() && ls.back().size() < sz){
            ls.back().push(val);
        }
        else{
            stack<int> tmp;
            tmp.push(val);
            ls.push_back(tmp);
        }
    }

    int pop() {
        if(sz == 0) return -1;
        if (ls.empty()) return -1;
        int ans = ls.back().top();
        ls.back().pop();
        if(ls.back().size()==0) ls.pop_back();
        return ans;
    }

    int popAt(int index) {
        if(sz == 0) return -1;
        if(index >= ls.size()) return -1;
        if(index == 0){
            int ans = ls.front().top();
            ls.front().pop();
            if(ls.front().size() == 0) ls.pop_front();
            return ans;
        }
        else{
            auto it = ls.begin();
            while(index --) ++it;
            int ans = it->top();
            it->pop();
            if(it->size() == 0) ls.erase(it);
            return ans;
        }
    }
};