#include <iostream>

using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;

    if (N > M) {
        int dif = N - M;
        if (dif == 1) {
            cout << "Dr. Chaz needs " << dif << " more piece of chicken!" << endl;
        }
        else {
            cout << "Dr. Chaz needs " << dif << " more pieces of chicken!" << endl;
        }
    }
    else {
        int dif = M - N;
        if (dif == 1) {
            cout << "Dr. Chaz will have " << dif << " piece of chicken left over!" << endl;
        }
        else {
            cout << "Dr. Chaz will have " << dif << " pieces of chicken left over!" << endl;
        }
    }
}