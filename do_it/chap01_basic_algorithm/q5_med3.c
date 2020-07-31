#include <stdio.h>

int		med3(int a, int b, int c)
{
	if ((b >= a && c <= a) || (b <= a && c >= a))
		return (a);
	else if ((a > b && c < b) || (a < b && c > b))
		return (b);
	return (c);
}

int		main(void)
{
	int a;
	int b;
	int c;

	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	printf("세 값의 중앙값은 %d입니다.", med3(a, b, c));
}
