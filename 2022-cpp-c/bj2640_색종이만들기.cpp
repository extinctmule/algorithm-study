#include <iostream>
#include <vector>
#include <cstdbool>

using namespace std;//필수

void go(const short& start, const short& now, bool arr[], const short& n, vector<short>& res)
{
	if (now == 1)
	{
		res[arr[start]]++; //if blue:1, white:0 

		return;
	}
	else
	{
		for (short i(start), tmp(arr[start]); i <= start + (now - 1) * n; i += n)
		{
			for (short j(0); j < now; j++)
			{
				if (tmp != arr[i + j])
				{
					short h_now = now / 2;

					go(start, h_now, arr, n, res);
					go(start + h_now, h_now, arr, n, res);
					go(start + h_now * n, h_now, arr, n, res);
					go(start + h_now * (n + 1), h_now, arr, n, res);

					return;
				}
			}
		}

		res[arr[start]]++;

		return;
	}
}


int main()
{

    //ios::sync_with_stdio(false); cin.tie(NULL);	cout.tie(NULL);//이거하면 4ms->0ms

	short n, now, start(0);
	vector<short> res(2, 0);

	cin >> n;
	now = n;

	bool arr[128 * 128];

	for (short i(0); i < n * n; i++)
	{
		cin >> arr[i];
	}

	go(start, now, arr, n, res);

	//
	cout << res[0] << '\n' << res[1];


	return 0;
}