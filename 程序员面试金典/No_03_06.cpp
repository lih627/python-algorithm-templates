class AnimalShelf {
    deque<vector<int> > dogs, cats;

public:
    AnimalShelf() {

    }

    void enqueue(vector<int> animal) {
        if(animal[1] == 0) cats.push_back(animal);
        else dogs.push_back(animal);
    }

    vector<int> dequeueAny() {
        if(dogs.empty()&& cats.empty()) return {-1, -1};
        if(dogs.empty() && !cats.empty()){
            auto ans = cats.front();
            cats.pop_front();
            return ans;
        }
        if(!dogs.empty() && cats.empty()){
            auto ans = dogs.front();
            dogs.pop_front();
            return ans;
        }
        if(dogs.front()[0] < cats.front()[0]){
            auto ans = dogs.front();
            dogs.pop_front();
            return ans;
        }
        else{
            auto ans = cats.front();
            cats.pop_front();
            return ans;
        }
    }

    vector<int> dequeueDog() {
        if (dogs.empty()) return {-1, -1};
        else {
            auto ans = dogs.front();
            dogs.pop_front();
            return ans;
        }
    }

    vector<int> dequeueCat() {
        if(cats.empty()) return {-1, -1};
        else{
            auto ans = cats.front();
            cats.pop_front();
            return ans;
        }
    }
};

/**
 * Your AnimalShelf object will be instantiated and called as such:
 * AnimalShelf* obj = new AnimalShelf();
 * obj->enqueue(animal);
 * vector<int> param_2 = obj->dequeueAny();
 * vector<int> param_3 = obj->dequeueDog();
 * vector<int> param_4 = obj->dequeueCat();
 */