#include <iostream>
#include <vector>
#include <string>

using namespace std;
using cs_t = const short;

void go(cs_t& start, cs_t& now, const vector<char>& arr, cs_t& n)
{
	if (now == 1)
	{
		cout << arr[start];//str.push_back(arr[start]);

		return;
	}
	else
	{
		for (short i(start), tmp(arr[start]); i < start + now * n; i += n)
		{
			for (short col(0); col < now; col++)
			{
				if (tmp != arr[i + col])
				{
					cout << '(';//str.push_back('(');//'(' 집어넣기

					short h_now = now * 0.5f;

					go(start, h_now, arr, n);
					go(start + h_now, h_now, arr, n);
					go(start + h_now * n, h_now, arr, n);
					go(start + h_now * (n + 1), h_now, arr, n);

					cout << ')';//str.push_back(')');//')' 집어넣기

					return;//이게 중요
				}
				else;
			}
		}

		cout << arr[start];//str.push_back(arr[start]);

		return;
	}
}

int main()
{
	ios::sync_with_stdio(false); cin.tie(NULL);	cout.tie(NULL);

	short n, now;

	cin >> n;
	now = n;

	vector<char> arr(n * n + 1);

	for (short i(0); i < n * n; i++)
	{
		cin >> arr[i];
	}

	short start(0);

	go(start, now, arr, n);

	return 0;
}