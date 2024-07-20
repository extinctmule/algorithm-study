#include <iostream>
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

using namespace std;

void merge(int* arr, int* sorted, const int& left, const int& right, const int& mid)
{
	int i(left), j(mid + 1), z(left);

	while (i <= mid && j <= right)
	{
		if (arr[i] <= arr[j])
			sorted[z++] = arr[i++];
		else
			sorted[z++] = arr[j++];
	}

	if (i > mid) {
		while (j <= right)
			sorted[z++] = arr[j++];
	}

	if (j > right) {
		while (i <= mid)
			sorted[z++] = arr[i++];
	}

	for (int e(left); e <= right; e++)
		arr[e] = sorted[e];
}

void devide(int* arr, int* sorted, const int& left, const int& right)
{
	int mid;

	if (left < right)
	{
		mid = (left + right) / 2;

		devide(arr, sorted, left, mid);
		devide(arr, sorted, mid + 1, right);

		merge(arr, sorted, left, right, mid);
	}
}

int main()
{
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int n;
	scanf("%d", &n);

	int* arr = new int[n] {0, };
	int* sorted = new int[n] {0, };

	for (int i(0); i < n; i++)
	{
		scanf("%d", arr + i);
	}

	int left(0), right(n - 1);
    
	devide(arr, sorted, left, right);

	for (int i(0); i < n; i++)
	{
		printf("%d\n", arr[i]);
	}

	return 0;
}