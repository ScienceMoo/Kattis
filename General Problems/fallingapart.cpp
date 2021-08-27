#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;

    int arr[n];

    for (int i = 0; i < n; i++) {
        int piece;
        cin >> piece;
        arr[i] = piece;
    }

    sort(arr, arr + n);

    int alice = 0;
    int bob = 0;
    bool turn = true;
    
    for (int i = n - 1; i >= 0; i--) {
        if (turn) {
            alice += arr[i];
        }
        else {
            bob += arr[i];
        }
        turn = !turn;
    }

    cout << alice << " " << bob << endl;
}