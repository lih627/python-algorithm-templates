class TripleInOne {
    int *stack;
    int top[3];
    int sz;
public:
    TripleInOne(int stackSize) {
       stack = new int[3 * stackSize];
       top[0] = -1;
       top[1] = stackSize - 1;
       top[2] = 2 * stackSize - 1;
       sz = stackSize;
    }

    void push(int stackNum, int value) {
        if (top[stackNum] == sz * (stackNum + 1) - 1)
            return;
        ++top[stackNum];
        stack[top[stackNum]] = value;
    }

    int pop(int stackNum) {
        if (top[stackNum] == sz * stackNum - 1) return -1;
        return stack[top[stackNum]--];
    }

    int peek(int stackNum) {
       if (top[stackNum] == sz * stackNum - 1)  return -1;
       return stack[top[stackNum]];

    }

    bool isEmpty(int stackNum) {
        return top[stackNum] == sz * stackNum - 1;

    }
};

/**
 * Your TripleInOne object will be instantiated and called as such:
 * TripleInOne* obj = new TripleInOne(stackSize);
 * obj->push(stackNum,value);
 * int param_2 = obj->pop(stackNum);
 * int param_3 = obj->peek(stackNum);
 * bool param_4 = obj->isEmpty(stackNum);
 */