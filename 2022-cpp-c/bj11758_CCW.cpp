#include <iostream>

using namespace std;

int main()
{
	int x1, y1, tmpx, tmpy, x2, y2;
	int shoelace, res;

	cin >> x1 >> y1;
	cin >> tmpx >> tmpy;
	cin >> x2 >> y2;

	//원점으로 정렬
	x1 -= tmpx;
	y1 -= tmpy;

	x2 -= tmpx;
	y2 -= tmpy;

	shoelace = x2 * y1 - x1 * y2;

	{
		if (shoelace > 0)
			res = 1;
		else if (shoelace < 0)
			res = -1;
		else
			res = 0;
	}

	cout << res;

	return 0;
}