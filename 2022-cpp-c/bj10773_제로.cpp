#include <iostream>
#include <stack>

using namespace std;

int main()
{
	ios::sync_with_stdio(false); cin.tie(NULL);	cout.tie(NULL);

	int k, sum(0);
	stack<int> st;

	cin >> k;

	for (int i(0), tmp; i < k; ++i)
	{
		cin >> tmp;

		if (tmp == 0)
		{
			sum -= st.top();
			st.pop();
		}
		else
		{
			sum += tmp;

			st.push(tmp);
		}
	}

	cout << sum;

	return 0;
}