#include <iostream>

using namespace std;

int main()
{
    int X;
    int N;
    cin >> X;
    cin >> N;

    int current = X;
    for (int i = 0; i < N; i++) {
        int p;
        cin >> p;
        current += X - p;
    }
    cout << current << endl;
}
