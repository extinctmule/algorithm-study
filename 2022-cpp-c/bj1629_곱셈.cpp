#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

long pow(const int& x, const int& m, const int& y)
{
	if (m == 1)
		return x;
	else
	{
		long tmp = pow(x, m / 2, y);

		if (m % 2)
			return (((tmp * tmp) % y) * x) % y;
		else
			return (tmp * tmp) % y;
	}
}

int main()
{
	ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

	int a, b, c;

	cin >> a >> b >> c;

	cout << pow(a % c, b, c);

	return 0;
}