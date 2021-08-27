#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    bool running = false;
    int previous = 0;
    int total = 0;

    for (int i = 0; i < n; i++) {
        int time;
        cin >> time;
        if (running) {
            total += time - previous;
        }
        running = !running;
        previous = time;
    }

    if (running) {
        cout << "still running" << endl;
    } else {
        cout << total << endl;
    }
}