#include <iostream>
#include <string>

using namespace std;

int main()
{
    int W, L;
    std::cin >> W >> L;
    int house = 1;

    while (W != 0 && L != 0) {
        int room[L][W];
        int entrance_x;
        int entrance_y;
        string line;
        std::getline(std::cin,line);
        for (int l = 0; l < L; l++) {
            string line;
            std::getline(std::cin,line);

            // cout << line << endl;
            for (int w = 0; w < W; w++) {
                char c = line[w];
                if (c == '*') {
                    entrance_x = l;
                    entrance_y = w;
                }
                room[l][w] = c;
            }
        }

        int direction_x = 1;
        int direction_y = 1;

        if (entrance_x == L-1) {
            direction_x = -1;
            direction_y = 0;
        }
        if (entrance_x == 0) {
            direction_y = 0;
        }
        if (entrance_y == 0) {
            direction_x = 0;
        }
        if (entrance_y == W-1) {
            direction_x = 0;
            direction_y = -1;
        }

        int current_x = entrance_x;
        int current_y = entrance_y;
        char current = '*';

        while (current != 'x') {
            current_x += direction_x;
            current_y += direction_y;

            current = room[current_x][current_y];
            if (current == '/') {
                int temp = direction_x;
                direction_x = - direction_y;
                direction_y = - temp;
            }
            if (current == '\\') {
                int temp = direction_x;
                direction_x = direction_y;
                direction_y = temp;
            }
            if (current == 'x') {
                room[current_x][current_y] = '&';
            }
        }

        cout << "HOUSE " << house << endl;

        for (int l = 0; l < L; l++) {
            string line;
            for (int w = 0; w < W; w++) {
                line += room[l][w];
            }
            cout << line << endl;
        }

        house += 1;
        std::cin >> W >> L;
    }
}