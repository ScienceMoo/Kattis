#include <iostream>

using namespace std;

int main()
{
    int wc, hc, ws, hs;
    cin >> wc >> hc >> ws >> hs;

    bool success = true;
    if (ws + 2 > wc) {
        success = false;
    }
    if (hs + 2 > hc) {
        success = false;
    }
    if (success) {
        cout << 1 << endl;
    }
    else {
        cout << 0 << endl;
    }
}