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
        int a,b,c;
        cin >> a >> b >> c;
        if (a == b){
            if (c%2 == 0){
                cout << "Second" << endl;
            }
            else{
                cout << "First" << endl;
            }
        }

        else{
            if (c%2 != 0){
                a = a-1;
                b = b;
            }

            if (a>b){
                cout << "First" << endl;
            }
            else{
                cout << "Second" << endl;
            }
        }


    }

    return 0;
}