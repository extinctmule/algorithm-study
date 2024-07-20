#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main()
{
	ios::sync_with_stdio(false); cin.tie(NULL);	cout.tie(NULL);
	int n;
	cin >> n;

	string tmp("abcdef");
	queue <int> commands;

	while (n--)
	{
		cin >> tmp;

		if (tmp == "push")//예외
		{
			int tmpi;
			cin >> tmpi;
			commands.push(tmpi);
		}
		else if (commands.empty())// 걍 empty 여부 먼저 나눠보자.. 근데 size는어디다처리..?
		{
			if (tmp == "size")
				cout << 0 << '\n';
			else if (tmp == "empty")
				cout << 1 << '\n';
			else//pop, front, back
				cout << -1 << '\n';
		}
		else
		{
			if (tmp == "pop")
			{
				cout << commands.front() << '\n';
				commands.pop();
			}
			else if (tmp == "size")
				cout << commands.size() << '\n';
			else if (tmp == "empty")
				cout << 0 << '\n';
			else if (tmp == "front")
				cout << commands.front() << '\n';
			else//back
				cout << commands.back() << '\n';
		}
	}
	return 0;
}