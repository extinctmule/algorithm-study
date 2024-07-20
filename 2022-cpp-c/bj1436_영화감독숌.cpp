#include <iostream>
#include <vector>

using namespace std;

int main()
{
	ios::sync_with_stdio(false); cin.tie(NULL);	cout.tie(NULL);

	int n, res(666);

	cin >> n;

	for (int cnt(1); cnt != n; )
	{
		++res;

		for (int tmp(res); tmp > 0; tmp *= 0.1f)
		{
			if (tmp % 1000 == 666)
			{
				++cnt;
				break;
			}
		}
	}

	cout << res;

	return 0;
}