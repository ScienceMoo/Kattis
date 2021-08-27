#include <iostream>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;

    int total = 0;
    for (int i = 0; i < k; i++) {
        int rating;
        cin >> rating;
        total += rating;
    }

    float factor =  3 * (n - k);

    cout << (total - factor) / n << " " << (total + factor) / n << endl;
}