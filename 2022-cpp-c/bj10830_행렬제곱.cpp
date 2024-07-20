#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
unsigned N;

vector<unsigned> mul(const vector<unsigned>& A, const vector<unsigned>& B)//매개변수 두개가맞는듯
{
	vector<unsigned> C(N * N);

	unsigned u;
	for (int iset(0), k(0); iset < N * N; iset += N)
	{
		for (int jset(0); jset < N; jset++, k++)
		{
			unsigned u(0);
			for (int i(iset), j(jset); j < N * N; i++, j += N)
				u += (A[i] * B[j]);

			C[k] = u % 1000;
		}
	}

	return C;
}

vector<unsigned> pow(const unsigned long long& now, const vector<unsigned> mat)
{
	if (now == 1)
		return mat;
	else
	{
		vector<unsigned> tmp(N * N);
		tmp = pow(now / 2, mat);

		if (now % 2)
			return mul(mul(tmp, tmp), mat);
		else
			return mul(tmp, tmp);
	}
}

int main()
{
	ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

	unsigned long long B;//이거 int로 대충하면 바로 틀렸습니다 뜬다
	cin >> N >> B;

	vector<unsigned> mat(N * N);

	for (int i(0); i < N * N; ++i)
	{
		cin >> mat[i];
		if (mat[i] == 1000)//중요;; 이거안하면 80%에서 틀렸다고 뜸
			mat[i] = 0;
	}

	vector<unsigned> res(N * N);
	res = pow(B, mat);


	for (int i(0), k(0); i < N; ++i)
	{
		for (int j(0); j < N; ++j, ++k)
			cout << res[k] << ' ';
		cout << '\n';
	}

	return 0;
}