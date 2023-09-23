#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>

using namespace std;

int main() {
    // int n = 8; // Length of the array
    // int M = 5; // Number of integers to pick
    // vector<int> A = {3, 4, 3, 8, 1, 15, 20, 3};

    int n, M;
    cin >> n >> M;
    int temp;
    vector<int> A;

    for (int i = 0; i < n; i++){
        cin >> temp;
        A.emplace_back(temp);
    }

    // Sort the array A in ascending order
    sort(A.begin(), A.end());

    int minDiff = INT_MAX; // Initialize the minimum difference
    int result = 0; // Initialize the result variable

    // Use a sliding window of size M to find the subarray with the minimum difference
    for (int i = 0; i <= n - M; i++) {
        int diff = A[i + M - 1] - A[i];
        if (diff < minDiff) {
            minDiff = diff;
            result = A[i];
        }
    }

    // Print the result
    cout << result << endl;

    return 0;
}