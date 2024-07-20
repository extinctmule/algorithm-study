#include <iostream>
#include <vector>
#include <string>

using namespace std;
int main()
{
	cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false);

	int r, c;
	cin >> r >> c;

	char lawn[503][503];

	lawn[0][0] = '\0';
	lawn[r + 1][0] = '\0';

	for (int i(1); i <= r; i++)
	{
		string tmp;
		cin >> tmp;

		lawn[i][0] = ' ';
		lawn[i][c + 1] = ' ';

		for (int j(1), jj(0); j <= c; j++, jj++)
		{
			lawn[i][j] = tmp[jj];
		}
	}

	for (int i(1); i <= r; i++)
	{
		for (int j(1); j <= c; j++)
		{
			if (lawn[i][j] == '.')
				lawn[i][j] = 'D';
			else if (lawn[i][j] == 'S')
			{
				if (lawn[i - 1][j] == 'W' || lawn[i + 1][j] == 'W' || lawn[i][j - 1] == 'W' || lawn[i][j + 1] == 'W')
				{
					cout << '0' << endl;

					return 0;
				}
			}
		}
	}

	cout << '1' << endl;

	for (int i(1); i <= r; i++)
	{
		for (int j(1); j <= c; j++)
			cout << lawn[i][j];
		cout << endl;
	}

	return 0;
}