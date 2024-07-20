#include <stdio.h>
//아니 근데 키는똑같은데 몸무게가 누가 더 나가면 걔네 둘은 같은등수인게 말이되나 왜케 신경쓰이지 ;;;;;

int main(void) {
	int n;

	int w[51];//몸무게
	int h[51];//키
	int rank;
	scanf("%d", &n);
	
	for(int i=1; i<=n; i++)
		scanf("%d %d", &w[i], &h[i]);
	
	for(int i=1; i<=n; i++){//당사자
		rank = 1;
		for(int j=1; j<=n; j++)//비교대상
			if(w[i]<w[j] && h[i]<h[j]) rank++;
		printf("%d ", rank);
	}
	return 0;
}
