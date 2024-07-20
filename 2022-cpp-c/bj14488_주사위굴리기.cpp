#include <iostream>
using namespace std;

int main()
{
	int n, m, k, top;
	int x, y;

	cin >> n >> m >> x >> y >> k;

	int* map = new int[n * m];
	int dice[7]{ 0, };
	//int switchTop[5][7] = { {0,0,0,0,0,0,0}, {0, 4, 4, 1, 6, 4, 4},{0, 3, 3, 6, 1, 3, 3},{0, 5, 1, 5, 5, 6, 2}, {0, 2, 6, 2, 2, 1, 5} };

	int nm = n * m;

	for (int i = 0; i < nm; i++)
		cin >> map[i];

	int newN = n - 1, newM = m - 1;

	for (int i = 0; i < k; i++)
	{
		{
			int top = dice[1];

			int tmp;
			cin >> tmp;

			if (tmp == 1)//동. 따라서 y값변화. (x로실수함)
			{
				if (y < newM)
				{
					y++;
					dice[1] = dice[4];
					dice[4] = dice[6];
					dice[6] = dice[3];
					dice[3] = top;
				}
				else continue;
			}
			else if (tmp == 2)//서
			{
				if (y > 0)
				{
					y--;
					dice[1] = dice[3];
					dice[3] = dice[6];
					dice[6] = dice[4];
					dice[4] = top;
				}
				else continue;
			}
			else if (tmp == 3)//북
			{
				if (x > 0)
				{
					x--;
					dice[1] = dice[2];
					dice[2] = dice[6];
					dice[6] = dice[5];
					dice[5] = top;
				}
				else continue;
			}
			else if (tmp == 4)//남
			{
				if (x < newN)
				{
					x++;
					dice[1] = dice[5];
					dice[5] = dice[6];
					dice[6] = dice[2];
					dice[2] = top;
				}
				else continue;
			}
		}

		int loc = x * m + y;

		if (map[loc]==0)
		{
			map[loc] = dice[6];
		}
		else
		{
			dice[6] = map[loc];
			map[loc] = 0;
		}

		cout << dice[1] << endl;
	}

	return 0;
}