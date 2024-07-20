#include <stdio.h>
#include <stdlib.h>

void merge(int a[], int mid, int n){
    int *s_a = (int*)malloc(n*4);
    int i =0, j=mid, k=0;
    while(i<mid && j<n){
        if(a[i] <= a[j]) s_a[k++] = a[i++];
        else s_a[k++] = a[j++];
    }
    while(i<mid) s_a[k++] = a[i++];
    while(j<n) s_a[k++]=a[j++];
    
    for(i=0; i<n; i++) a[i]=s_a[i];
    free(s_a);
}
void merge_sort(int a[], int n){
    int mid;
    if(n!=1){
        mid = n/2;
        merge_sort(a,mid);
        merge_sort(a+mid,n-mid);
        merge(a,mid,n);
    }
}
int main() {
	int n, m1, m2, m3, m4, check = 0;
	int i,j,g, sum=0;
	scanf("%d", &n);
	int *a = (int*)malloc(n*4);
	for (g = 0; g < n; g++){
		scanf("%d", &a[g]);
		sum += a[g];
	}
	float res = sum;
	res /= (float)n;

	if (res < 0) {
		check = 1;
		res = -res;
	}
	if (res - (int)res >= 0.5) res += 1;
	if (check) res = -res;
	m1 = (int)res;
	//m1
	
    merge_sort(a,n);
	m3 = a[1];
	if (n == 1) m3 = a[0];
	else{
		int check = 0;
		int most=1;
		int t = n-1;
		for (i = 0; i < t;) {
			j = 1;
			while (a[i] == a[i + 1]) {
				i++;
				j++;
			}
			if (j > 1 && j >= most) {
				if (j > most) {
					most = j;
					m3 = a[i];
					check = 0;
				}
				else if (check==0) {
					m3 = a[i];
					check = 1;
				}
			}
			i++;
		}
	}//m3
	m2 = a[n / 2];
	m4 = a[n - 1] - a[0];
	printf("%d\n%d\n%d\n%d\n", m1, m2, m3, m4);
    free(a);
	return 0;
}