#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        int current_day = 0;
        int count = 0;
        int days, M;
        cin >> days >> M;

        for (int m = 0; m < M; m++) {
            int d;
            cin >> d;

            if (d >= 13) {
                if ((current_day + 12) % 7 == 5) {
                    count += 1;
                }
            }
            current_day += d;
        }

        cout << count << endl;
    }
}