#include <iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(false); cin.tie(NULL);	cout.tie(NULL);

	int n, k;

	cin >> n >> k;

	if (k == 0)
	{
		while (n--)
			cout << 'B';

		return 0;
	}
	else
	{
		int k_d_2, maxK, front(0);

		if (n % 2 == 1)
		{

			k_d_2 = n * 0.5f;
			maxK = k_d_2 * (k_d_2 + 1);

			if (k > maxK)
			{
				cout << -1;

				return 0;
			}
			else if (k == maxK)
			{
				for (int i(0); i < k_d_2; i++)
					cout << 'A';
				for (int i(0); i < k_d_2 + 1; i++)
					cout << 'B';

				return 0;
			}
		}
		else
		{
			k_d_2 = n * 0.5f;
			maxK = k_d_2 * k_d_2;

			if (k > maxK)
			{
				cout << -1;

				return 0;
			}
			else if (k == maxK)
			{
				for (int i(0); i < k_d_2; i++)
					cout << 'A';

				for (int i(0); i < k_d_2; i++)
					cout << 'B';

				return 0;
			}
		}

		do
		{
			++front;
		} while (k >= front * (n - front));

		int gap = front * (n - front) - k;
		//front + gap

		for (int i(1); i <= front - 1; i++)
			cout << 'A';

		for (int i(1); i <= gap; i++)
			cout << 'B';

		cout << 'A';

		for (int i(1); i <= n - front - gap; i++)
			cout << 'B';
	}

	return 0;
}