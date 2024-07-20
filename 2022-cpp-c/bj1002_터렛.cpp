#include <iostream>
#include <array>
#include <cmath>

using namespace std;

int main()
{
	array <long, 3> cho;
	array <long, 3> baek;

	int testcase;

	cin >> testcase;

	while (testcase--)
	{
		cin >> cho[0] >> cho[1] >> cho[2] >> baek[0] >> baek[1] >> baek[2];

		int res;
		array<long, 3>& small(cho), & large(baek);

		if (baek[2] <= cho[2])
			swap(small, large);

		/*바보코드
		array<long, 3>& small(cho), & large(baek);

		if (baek[2] <= cho[2])
		{
			small = baek;
			large = cho;
		}

		*/
		// 오늘의 교훈: 레퍼런스 어레이에 쓸땐 좀 생각좀 잘 좀 하고 쓰자
		// swap 내가 구현하려고 하지말고 걍 함수 쓰자

		// 실용적인교훈: 채점중 50% 에서 틀렸는데 이거아마 반지름 small large 테스트케이스 나눠서 채점하는것인듯?


		if (small[0] == large[0] && small[1] == large[1])//중심점같음
		{
			if (small[2] == large[2])//반지름같음
				res = -1;
			else
				res = 0;
		}
		else//중싱점 다름
		{
			long plus = small[2] + large[2];
			long minus = large[2] - small[2];
			long dist_2 = small[0] - large[0];
			dist_2 *= dist_2;
			dist_2 += (small[1] - large[1]) * (small[1] - large[1]);

			long RMinusR_2 = minus * minus;
			long RPlusR_2 = plus * plus;

			if (dist_2 < RMinusR_2)
				res = 0;
			else if (dist_2 > RPlusR_2)
				res = 0;
			else if (dist_2 == RPlusR_2)
				res = 1;
			else if (dist_2 == RMinusR_2)
				res = 1;
			else// (dist + small[2] < large[2])
				res = 2;
		}

		cout << res << endl;
	}

	return 0;
}