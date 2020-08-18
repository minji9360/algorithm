#include <stdio.h>

int main(void) 
{
	int A;
	int B;

	scanf("%d", &A);
	scanf("%d", &B);
    if (A > 0 && B < 10) 
    {
        printf("%d", A + B); 
    } 
    else 
    {
		printf("A는 0보다 크고 B는 10보다 작아야 합니다.");
    }
}

