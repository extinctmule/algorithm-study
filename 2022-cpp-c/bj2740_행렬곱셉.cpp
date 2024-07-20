#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int r1, c1;
	cin >> r1 >> c1;

	int sizeA = r1 * c1;

	vector<int> A;

	A.reserve(10000);
	A.resize(sizeA);
    

	for (int i(0); i < sizeA; i++)
	{
		cin >> A[i];
	}

	int r2, c2;
	cin >> r2 >> c2;
    int sizeB = r2*c2;
    
    vector<int> B;
    B.reserve(10000);
    B.resize(sizeB);

	for (int i(0); i < sizeB; i++)
	{
		cin >> B[i];
	}


	for (int iset(0); iset < sizeA; iset += c1)
	{
		for (int jset(0); jset < c2; jset++)
		{
			int tmp(0);

			for (int i(iset), j(jset); j<sizeB; i++, j += c2)
			{
				tmp += (A[i] * B[j]);
			}
            
			cout << tmp << " ";//Res[] 사용하지말아보자
		}

		cout << endl;
	}


	return 0;
}