#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    for (int i = 0; i < n; i++){
        string w;
        cin >> w;

        int l;
        l = w.length();

        if (l <= 10){
            cout << w << "\n";
        }
        else{
            cout << w[0] << l-2 << w[l-1] << "\n";
        }
    }

    return 0;
}