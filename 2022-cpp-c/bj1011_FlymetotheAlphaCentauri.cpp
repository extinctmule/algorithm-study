#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false);

	int testcase;

	cin >> testcase;

	while (testcase--)
	{
		long x, y, res;

		cin >> x >> y;

		double dif(y - x);

		double d_tmp = sqrt(dif);
		long l_tmp = (long)d_tmp;//정수

		if (d_tmp == l_tmp)
			res = 2 * l_tmp - 1;
		else if (dif <= l_tmp * (l_tmp + 1))
			res = 2 * l_tmp;
		else
			res = 2 * l_tmp + 1;

		cout << res << endl;
	}

	return 0;
}