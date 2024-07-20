//https://www.acmicpc.net/board/view/67181
//short 떄매 런타임에러 outofbounds나서 계속 틀림
//다음부턴 테스트케이스 최대n으로도 해보자..
#include <iostream>
#include <vector>

using namespace std;

using ci_t = const int;

int arr[2187 * 2187];
int res[3] = { 0 };

void go(ci_t& start, ci_t& now, ci_t& n)
{
	if (now == 1)
	{
		res[arr[start] + 1]++;

		return;
	}
	else
	{
		for (int i(start), tmp(arr[start]); i < start + now * n; i += n)
		{
			for (int col(0); col < now; col++)
			{
				if (tmp != arr[i + col])
				{

					for (int line(start), now3(now / 3); line < start + now * n; line += n * now3)
					{
						for (int col(0); col < now; col += now3)
						{
							go(line + col, now3, n);
						}
					}

					return;//이게 중요
				}
				else;
			}
		}

		res[arr[start] + 1]++;

		return;
	}
}

int main()
{
	ios::sync_with_stdio(false); cin.tie(NULL);	cout.tie(NULL);

	int n, now;

	cin >> n;

	for (int i(0); i < n * n; i++)
	{
		cin >> arr[i];
	}

	now = n;
	go(0, now, n);

	cout << res[0] << '\n' << res[1] << '\n' << res[2];

	return 0;
}