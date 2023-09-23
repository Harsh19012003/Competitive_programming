#include <bits/stdc++.h>
#include <vector>
#include <map>

using namespace std;

int main(){

    // for fast input output
    ios::sync_with_stdio(0);
    cin.tie(0);
    

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int size;
        cin >> size;
        vector<int> x;

        for(int i = 0; i < size; i++){
            int a;
            cin >> a;
            x.push_back(a);
        }
        int output = 0;
        for (int i = 0; i < size-1; i++){
            if (x[i] > x[i+1]){
                output = size - i;
                break;
            }
        }

        
        cout << output << endl;
    }

    return 0;
}