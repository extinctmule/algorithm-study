#include <iostream>
#include <string>
using namespace std;

int main()
{
	unsigned int x, y, dif, days;
	unsigned int i(1);

	cin >> x >> y;

	dif = y - x;

	if (dif == 0)
	{
		cout << 0;
		return 0;
	}

	for (i = 1; ; ++i)
	{
		int tmp = i * i;

		if (tmp >= dif)
		{

			tmp = i * i - i;
	
			if (tmp < dif)
				days = i * 2 - 1;
			else
				days = i * 2 - 2;
			break;
		}
		else;
	}

	cout << days << endl;

	return 0;
}