#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main(){

    vector<int> vec = {1,1,1,1,2,3,3,4,4,5,5,5,6};
    for(int i = 0; i < vec.size(); i++){
        cout << vec[i];
    }

    cout << endl;

    for(int p = 0; p < vec.size(); p++){
        // if(vec[p] == 1){
            remove(vec.begin(), vec.end(), 1);
            cout << "vec size becomes: " << vec.size();
        // }
    }

    cout << endl;
    for(int j: vec){
        cout << j;
    }

    return 0;
}