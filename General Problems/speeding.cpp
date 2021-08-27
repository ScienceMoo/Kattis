
#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    float highest = 0;

    int previous_t = 0;
    int previous_d = 0;

    for (int i = 0; i < n; i++) {
        int t,d;
        cin >> t >> d;

        float dist = d - previous_d;
        float time = t - previous_t;
        float speed = dist / time;
        if (speed > highest) {
            highest = speed;
        }
        previous_d = d;
        previous_t = t;
    }

    int result = (int) highest;
    
    cout << result << endl;
}