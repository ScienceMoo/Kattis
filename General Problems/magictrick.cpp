#include <iostream>

using namespace std;

int main()
{
    string s;
    cin >> s;

    bool success = true;
    for (int i = 0; i < s.size(); i++) {
        for (int j = i + 1; j < s.size(); j++) {
            if (s[i] == s[j]) {
                success = false;
                break;
            }
        }
    }
    if (success) {
        cout << 1 << endl;
    }
    else {
        cout << 0 << endl;
    }
}