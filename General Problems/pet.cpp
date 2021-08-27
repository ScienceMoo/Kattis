#include <iostream>

using namespace std;

int main()
{
    int highest = 0.0;
    int winner = 1;
    for (int i = 1; i <= 5; i++) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        int rating = a + b + c + d;
        if (rating > highest) {
            highest = rating;
            winner = i;
        }
    }


    cout << winner << " " << highest << endl;
}