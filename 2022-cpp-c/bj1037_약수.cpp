#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

int main()
{
	int divisors_num;
	cin >> divisors_num;

	//vector<unsigned> divisors;
	//divisors.reserve(50);
	//divisors.resize(divisors_num);

	int min_divisor(1000000), max_divisor(1);//min and max can be same.

	while (divisors_num--)
	{
		int int_tmp;
		cin >> int_tmp;
		min_divisor = min(min_divisor, int_tmp);
		max_divisor = max(max_divisor, int_tmp);
	}

	unsigned long N = min_divisor * max_divisor;

	cout << N;


	return 0;
}