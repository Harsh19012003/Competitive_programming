#include <bits/stdc++.h>
#include <array>
#include <vector>
using namespace std;

int main(){
    int number;
    cin >> number;
    vector <int> x;

    for(int i = 0; i < number; i++){
        int temp;
        cin >> temp;
        x.push_back(temp);
    }

    for(int i = 0; i < x.size(); i++){
        cout << "-" << x[i] << "\n";
    }

    // for(int i = x.size()-1; i > 0; i--){
    //     for(int j = i-1; j > 0; j--){
            
    //         cout << "i and j : " << i << j << endl;
    //         if (x[i] == x[j] && i != j){
    //             "erasing this \n";
    //             x.erase(x.begin()+i);
    //         }
    //     }
    // }


    //////////////////////////////////////////////////// 


    
    // for (int i = 0; i < x.size(); i++){
    //     cout << "i == " << i;

    //     for (int j = i; j < x.size(); j++) {
    //         cout << " j == "<< j;

    //         if (i != j && x[i] == x[j]){
    //             // int tem = x.begin()+i;
    //             cout << " erasing this index == " << i << j << " with this val == " << x[i];
    //             x.erase(x.begin()+i);
    //         }
    //     }
    // }



    for (int i: x){
        cout << "i == " << i;

        for (int j: x) {
            cout << " j == "<< j << endl;

            if (i == j){
                // int tem = x.begin()+i;
                cout << " erasing this index == " << i << j << " with this val == " << x[i] << endl;
                x.erase(x.begin()+i); 
            }
        }
    }

    cout << "\n";

    for(int i = 0; i < x.size(); i++){
        cout << "+" << x[i] << "\n";
    }
    return 0;
}
