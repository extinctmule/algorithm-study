#include <iostream>

#include <cmath>

using namespace std;

unsigned go(unsigned N, unsigned *arr)
{
	if (N == 1)
		return 0;
	else
	{
		if (arr[N])
			return arr[N];//이미 구했다면 아래과정 스킵
		else
		{
			arr[N] = go(N - 1, arr) + 1;

			if (N % 2 == 0)
			{
				unsigned tmp = go(N / 2, arr) + 1;

				arr[N] = min(arr[N], tmp);
			}

			if (N % 3 == 0)
			{
				unsigned tmp = go(N / 3, arr) + 1;

				arr[N] = min(arr[N], tmp);
			}

			return arr[N];
		}

	}

	//return arr[N]; 이거 위치 어디가 적합?
}

int main()
{
	unsigned N, res(1);
	unsigned count(0);
	
	cin >> N;

	unsigned* arr = new unsigned[N + 1]{ 0, };

	go(N, arr);

	cout << arr[N] << endl;

	return 0;
}
