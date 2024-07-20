#include <stdio.h>

int main() {
	int c=1, n, res, tmp, sixnine, max;
	int zeroNine[10] = { 0 };
	int* pW = zeroNine, * pL = zeroNine + 9;

	scanf("%d", &n);
	res = n;
	while (res) {
		tmp = res% 10;
		res /= 10;
		(*(pW + tmp))++;
	}

	sixnine = (pW[6] + pW[9] + 1) / 2;//홀수면 +1
	pW[6] = 0;
	pW[9] = 0;
	
	max = *pW;
	for (pW++; pW<=pL; pW++)
		if (max < *pW) max = *pW;
	if (max<sixnine) max = sixnine;
		printf("%d\n", max);
	return 0;
}