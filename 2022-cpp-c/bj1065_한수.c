#include <stdio.h>
void hansoo(int N);
int main(){
    int N;
    scanf("%d", &N);
    hansoo(N);
    return 0;
}
void hansoo(int N){
    int num = 0;
    if (N<100)
        printf("%d\n", N);
    else{
        num = 99;
        for (int i=100; i<=N; i++){
            if ( 2*((i/10)%10) == i%10 + i/100 )
                num++;
        }
        printf("%d\n", num);
    }
    return;
}