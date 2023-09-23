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
        int total, z, no_z, no_one;
        cin >> total >> z >> no_one >> no_z;
        int req_z, req_one, cost;
        cout << "initial";

        if (no_z == 0){
            req_z = 1;
            req_one = total;
        }
        else{
            req_z = total/no_z;
            req_one = total%no_z;
        }
        req_z = total/no_z;
        req_one = total%no_z;
        int no_f_one= std::numeric_limits<int>::max(), no_f_z= std::numeric_limits<int>::max();
        int req_f_z, req_f_one;
        if(req_z <= no_z){
            cout << "X";

            if (req_one <= no_one){
                cout << "A";
                cout << no_z << "\t" << "ho gaya" << "\n";
                return 0;
            }
            else {
                cout << "B";
                cost = total - req_z - req_one;
                req_f_z = total/no_z;
                req_f_one = total%no_z;
                cout << "fancy coins:" << req_f_z + req_f_one << endl;
                // CALCULATE FANCY
            }
        }


        else {
            cout << "Y";
            cost = total - no_z*z;
            cout << "cost: " << cost << "\n";
            
            if (no_one >= cost){
                cout << "C";

                cout << no_z << "\t" << "ho gaya" << "\n";
                return 0;
            }
            else {
                cout << "D";

                cost = total - req_z*z - req_one;
                req_f_z = cost/no_z;
                req_f_one = cost%no_z;
                cout << "fancy coins:" << req_f_z + req_f_one << endl;
            }
        }
    }

    return 0;
}
