#include <bits/stdc++.h>


using namespace std

    ;
int main(){
    int input[] = {1,2,3,4,-1,3,2,-1,0,-4};

    #define f(a,b) for (int i = a; i < b; i++)

    int n = sizeof(input)/sizeof(int);


    for (int i = 0; i < n; i++){
        for (int j = i; j < n; j++){
            int sum = 0;
            for (int k = i; k < j+1; k++){
                sum += input[k];
            }
            cout << sum << "\n";
        }
    }

    return 0;
}
