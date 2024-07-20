#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <string>

using namespace std;

//

//void pop(CheckChar_& CheckChar) {
//
//	CheckChar.stack.pop_back();
//	//CheckChar.stack.erase(CheckChar.cnt - 1);
//
//	CheckChar.cnt--;
//	//CheckChar.stack.resize(CheckChar.cnt);


int main() {

	while (1)
	{
		string str;
		str.reserve(101);

		getline(cin, str);

		bool sym = 1;
		stack<char> Stack;

		//if()


		//종료조건 '.'
		if ((str.size() == 1) && str[0] == '.')
			break;


		for (int i = 0; i < str.size(); i++)
		{

			if (str[i] == '(' || str[i] == '[')
			{
				Stack.push(str[i]);
			}
			else;

			if (str[i] == ')')
			{
				if ((Stack.empty()) || Stack.top() == '[')
					sym = 0;
				else
					Stack.pop();

			}
			else if (str[i] == ']')
			{
				if ((Stack.empty()) || Stack.top() == '(')
					sym = 0;

				else
					Stack.pop();

			}
		}//for

		if ((Stack.empty()) && sym)
			cout << "yes" << endl;
		else
			cout << "no" << endl;


	}

	return 0;
}