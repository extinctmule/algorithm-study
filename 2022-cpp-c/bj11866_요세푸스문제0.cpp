#include <iostream>
#include <cstdlib>
using namespace std;

int main()
{
	int n, k;
	int* arr;

	cin >> n >> k;

	arr = (int*)malloc((n+1)*sizeof(int));
	
	arr[0] = -1;
	for (int i = 1; i <= n; i++)
		arr[i] = i;

	cout << '<';

	int count(n);
	int out(0);
	do {
		int k2(k);
		do{
			out++;
			out = (out > n) ? out - n : out;
			if (arr[out] == 0)
			{
				continue;
			}
			k2--;
		} while (k2);
		count--;
		cout << arr[out];

		if (count > 0)
			cout << ", ";

		arr[out] = 0;
	} while (count);

	cout << '>' << endl;

	return 0;
}