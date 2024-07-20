#include <iostream>
#include <algorithm>
//#include <array>
//#include <vector>
//#include <cassert>
//#include <string>
using namespace std;

typedef char phew[6563];

phew* my2D = new phew[6563]{};

struct _LocInfo {
	int side;
	int r;
	int c;
};

void putBlank(_LocInfo& L)
{
	const int& side = L.side;
	const int& r = L.r, & c = L.c;

	for (int i = L.r; i < L.r + side; i++)
	{
		for (int j = L.c; j < L.c + side; j++)
		{
			my2D[i][j] = ' ';
		}
	}
}

int main()
{
	int n;

	cin >> n;

	{
		//initialization to '*'
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				my2D[i][j] = '*';
			}
		}
	}

	_LocInfo L{ n / 3, n / 3,n / 3 };

	for (int i = n; i >= 1; i /= 3)
	{
		//int& r = L.r, & c = L.c;

		for (L.r = i / 3; L.r < n; L.r += i)
		{
			for (L.c = i / 3; L.c < n; L.c += i)
			{
				putBlank(L);
			}
		}
		L.side /= 3;
	}


	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < n; c++)
		{
			cout << my2D[r][c];
		}
		cout << endl;
	}

	return 0;
}