#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;

    int total = 0;
    for (int i = 0; i < N; i++) {
        int l;
        cin >> l;
        total += l;
    }
    total -= (N - 1);
    cout << total << endl;
}